import json
from datetime import datetime
from pathlib import Path

from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.core.management.color import no_style
from django.db import connection, transaction
from django.db.migrations.executor import MigrationExecutor

from apps.repositorio.models import (
    AreaTematica,
    SubAreaTematica,
    Autor,
    Projeto,
    Registro,
    Status,
    Subprojeto,
    Tag,
    TipoDocumento,
    TipoPublicacao,
)


BASE_DIR = Path(__file__).resolve().parents[4]
DATA_DIR = BASE_DIR / 'www' / 'json_carga'
SQL_PATH = BASE_DIR / 'www' / 'sql_carga' / 'carga_inicial.sql'
JSON_PATH = DATA_DIR / 'carga_json.json'
EXPECTED_RECORDS = 457


class Command(BaseCommand):
    help = 'Limpa e repopula o app repositorio a partir das cargas atuais.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Valida o banco e as cargas sem alterar dados.',
        )
        parser.add_argument(
            '--apply',
            action='store_true',
            help='Executa a limpeza e a repopulação.',
        )
        parser.add_argument(
            '--confirm-repopulate',
            action='store_true',
            help='Confirma a operação destrutiva exigida com --apply.',
        )
    def handle(self, *args, **options):
        if options['apply'] == options['dry_run']:
            raise CommandError('Informe exatamente uma opção: --dry-run ou --apply.')
        if options['apply'] and not options['confirm_repopulate']:
            raise CommandError(
                'A operação destrutiva exige --confirm-repopulate.'
            )

        items = self.validate_environment()
        self.stdout.write(
            self.style.SUCCESS(
                f'Validação concluída: PostgreSQL, {len(items)} itens no JSON, '
                'usuário de auditoria disponível.'
            )
        )

        if options['dry_run']:
            self.report_dry_run(items)
            return

        with transaction.atomic():
            self.clear_repository()
            self.load_reference_sql()
            self.reset_sequences()
            self.ensure_references(items)
            self.reset_sequences()
            auditor_user = self.get_auditor_user()
            imported = self.import_records(items, auditor_user)
            self.reset_sequences()  # Garante que as sequências fiquem sincronizadas após a importação final

        self.stdout.write(
            self.style.SUCCESS(
                f'Repopulação concluída: {imported} registros importados.'
            )
        )
        self.report_counts()

    def validate_environment(self):
        if connection.vendor != 'postgresql':
            raise CommandError(f'Banco inesperado: {connection.vendor}. Esperado: postgresql.')

        executor = MigrationExecutor(connection)
        if executor.migration_plan(executor.loader.graph.leaf_nodes()):
            raise CommandError('Há migrations pendentes; operação abortada.')

        if not self.get_auditor_user():
            raise CommandError('Nenhum usuário ativo disponível para auditoria.')
        if not SQL_PATH.is_file():
            raise CommandError(f'Arquivo SQL não encontrado: {SQL_PATH}')
        if not JSON_PATH.is_file():
            raise CommandError(f'Arquivo JSON não encontrado: {JSON_PATH}')
        try:
            items = json.loads(JSON_PATH.read_text(encoding='utf-8'))
        except (OSError, json.JSONDecodeError) as error:
            raise CommandError(f'Não foi possível ler o JSON: {error}') from error

        if len(items) != EXPECTED_RECORDS:
            raise CommandError(
                f'Quantidade inesperada no JSON: {len(items)}; '
                f'esperado: {EXPECTED_RECORDS}.'
            )
        required_keys = {
            'PROJETO', 'SUBPROJETO', 'AUTOR', 'TITULO', 'DATA',
            'TIPO_DOCUMENTO', 'AREA_TEMATICA', 'STATUS', 'TIPO_PUBLICACAO',
            'LINK_REAL', 'TAGS',
        }
        for index, item in enumerate(items):
            missing = required_keys - item.keys()
            if missing:
                raise CommandError(
                    f'Item {index} do JSON sem campos: {sorted(missing)}'
                )
        return items

    def get_auditor_user(self):
        user_model = get_user_model()
        return (
            user_model.objects.filter(is_superuser=True, is_active=True).first()
            or user_model.objects.filter(is_active=True).first()
        )

    def report_dry_run(self, items):
        current_records = Registro.objects_all.count()
        current_autores = Autor.objects_all.count()
        current_tipo_documentos = TipoDocumento.objects_all.count()
        current_projetos = Projeto.objects_all.count()
        current_subprojetos = Subprojeto.objects_all.count()
        current_areas = AreaTematica.objects_all.count()
        current_subareas = SubAreaTematica.objects_all.count()
        current_tipo_publicacoes = TipoPublicacao.objects_all.count()
        current_tags = Tag.objects_all.count()
        current_users = get_user_model().objects.count()

        self.stdout.write('DRY-RUN')
        self.stdout.write(f'registros atuais={current_records}')
        self.stdout.write(f'registros esperados={len(items)}')
        self.stdout.write(f'subáreas atuais={current_subareas}')
        self.stdout.write(f'subprojetos atuais={current_subprojetos}')
        self.stdout.write(f'projetos atuais={current_projetos}')
        self.stdout.write(f'áreas temáticas atuais={current_areas}')
        self.stdout.write(f'autores atuais={current_autores}')
        self.stdout.write(f'tipo de documentos atuais={current_tipo_documentos}')
        self.stdout.write(f'tipo de publicações atuais={current_tipo_publicacoes}')
        self.stdout.write(f'tags atuais={current_tags}')
        self.stdout.write(f'usuários preservados={current_users}')
        self.stdout.write('Nenhuma alteração foi executada.')

    def clear_repository(self):
        through_tables = (
            Registro.subareas_tematicas.through,
            Registro.autores.through,
            Registro.tags.through,
        )
        for through_model in through_tables:
            through_model.objects.all().delete()

        Registro.objects_all.all().delete()
        Subprojeto.objects_all.all().delete()
        Projeto.objects_all.all().delete()
        apps.get_model('repositorio', 'SubAreaTematica').objects_all.all().delete()
        Autor.objects_all.all().delete()
        Tag.objects_all.all().delete()
        TipoDocumento.objects_all.all().delete()
        AreaTematica.objects_all.all().delete()
        Status.objects_all.all().delete()
        TipoPublicacao.objects_all.all().delete()

    def load_reference_sql(self):
        with connection.cursor() as cursor:
            cursor.execute(SQL_PATH.read_text(encoding='utf-8'))

    def reset_sequences(self):
        models = [
            apps.get_model('repositorio', model_name)
            for model_name in (
                'Projeto', 'Subprojeto', 'Autor', 'Tag', 'TipoDocumento',
                'AreaTematica', 'SubAreaTematica', 'Status', 'TipoPublicacao',
                'Registro', 'FotoGaleria',
            )
        ]
        sequence_sql = connection.ops.sequence_reset_sql(
            no_style(),
            models,
        )
        with connection.cursor() as cursor:
            for statement in sequence_sql:
                cursor.execute(statement)

    def ensure_references(self, items):
        for item in items:
            projeto, _ = Projeto.objects.get_or_create(
                nome=item['PROJETO'],
                defaults={'ativo': True},
            )
            Subprojeto.objects.get_or_create(
                projeto=projeto,
                nome=item['SUBPROJETO'],
                defaults={'ativo': True},
            )
            TipoDocumento.objects.get_or_create(
                nome=item['TIPO_DOCUMENTO'],
                defaults={'ativo': True},
            )
            AreaTematica.objects.get_or_create(
                nome=item['AREA_TEMATICA'],
                defaults={'ativo': True},
            )
            Status.objects.get_or_create(
                nome=item['STATUS'],
                defaults={'ativo': True, 'is_public': True},
            )
            TipoPublicacao.objects.get_or_create(
                nome=item['TIPO_PUBLICACAO'],
                defaults={'ativo': True},
            )
            for name in self.split_values(item.get('AUTOR', '')):
                Autor.objects.get_or_create(nome=name, defaults={'ativo': True})
            for name in self.split_values(item.get('TAGS', ''), clean_punctuation=True):
                Tag.objects.get_or_create(nome=name, defaults={'ativo': True})

    def import_records(self, items, auditor_user):
        for index, item in enumerate(items, start=1):
            projeto = Projeto.objects.get(nome=item['PROJETO'])
            subprojeto = Subprojeto.objects.get(
                projeto=projeto,
                nome=item['SUBPROJETO'],
            )
            tipo_documento = TipoDocumento.objects.get(nome=item['TIPO_DOCUMENTO'])
            area_tematica = AreaTematica.objects.get(nome=item['AREA_TEMATICA'])
            status = Status.objects.get(nome=item['STATUS'])
            tipo_publicacao = TipoPublicacao.objects.get(nome=item['TIPO_PUBLICACAO'])

            data_publicacao = self.parse_date(item['DATA'])
            link_real = (item.get('LINK_REAL') or '').strip()
            link_externo = link_real if (
                'LINK' in tipo_publicacao.nome.upper() or link_real.startswith('http')
            ) else None
            if link_externo:
                arquivo = None
            else:
                filename = link_real.lstrip('/')
                if not filename.lower().endswith('.pdf'):
                    filename = f'{filename}.pdf'

                # Preserva o caminho caso já esteja na estrutura padrão de uploads
                if filename.startswith('repositorio/'):
                    arquivo = filename
                else:
                    arquivo = f'repositorio/old_files/{filename}'

            registro = Registro.objects.create(
                subprojeto=subprojeto,
                tipo_documento=tipo_documento,
                titulo=item['TITULO'],
                area_tematica=area_tematica,
                status=status,
                tipo_publicacao=tipo_publicacao,
                data_publicacao=data_publicacao,
                arquivo=arquivo,
                link_externo=link_externo,
                usuario_criacao=auditor_user,
                usuario_ultima_atualizacao=auditor_user,
                ativo=True,
            )

            autor_names = self.split_values(item.get('AUTOR', ''))
            tag_names = self.split_values(item.get('TAGS', ''), clean_punctuation=True)
            autores = [Autor.objects.get(nome=name) for name in autor_names]
            tags = [Tag.objects.get(nome=name) for name in tag_names]
            registro.autores.set(autores)
            registro.tags.set(tags)

            if index % 100 == 0 or index == len(items):
                self.stdout.write(f'Importados: {index}/{len(items)}')
        return len(items)

    @staticmethod
    def split_values(value, clean_punctuation=False):
        values = [part.strip() for part in value.split(';') if part.strip()]
        if ',' in value and ';' not in value:
            values = [part.strip() for part in value.split(',') if part.strip()]
        if clean_punctuation:
            values = [part.replace(',', '').replace('.', '') for part in values]
        return values

    @staticmethod
    def parse_date(value):
        if not value:
            return None
        for date_format in ('%d/%m/%Y', '%m/%Y'):
            try:
                return datetime.strptime(value, date_format).date()
            except ValueError:
                continue
        raise CommandError(f'Data inválida: {value}')

    def report_counts(self):
        self.stdout.write(
            'CONTAGENS '
            f'projetos={Projeto.objects_all.count()} '
            f'subprojetos={Subprojeto.objects_all.count()} '
            f'autores={Autor.objects_all.count()} '
            f'tags={Tag.objects_all.count()} '
            f'registros={Registro.objects_all.count()} '
            f'usuarios={get_user_model().objects.count()}'
        )

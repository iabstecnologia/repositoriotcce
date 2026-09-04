import csv
import re
import unicodedata
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from apps.repositorio.models import Projeto, Registro, Subprojeto


CSV_PATTERN = 'Lista de Projetos TCCE*.csv'


def normalizar_texto(valor):
    valor = unicodedata.normalize('NFKD', valor)
    valor = ''.join(char for char in valor if not unicodedata.combining(char))
    return re.sub(r'\s+', ' ', valor).strip().upper()


def normalizar_tcce(valor):
    return re.sub(r'^TCCE\s*-\s*', 'TCCE ', normalizar_texto(valor))


def extrair_codigo(valor):
    match = re.search(r'(\d+(?:\.\d+)*(?:\s*\([^)]*\))?)', valor)
    if not match:
        raise CommandError(f"Código de subprojeto inválido: {valor}")
    codigo = match.group(1).strip()
    if codigo.isdigit():
        return str(int(codigo))
    return normalizar_texto(codigo)


def carregar_linhas(base_dir):
    for caminho in sorted(base_dir.glob(CSV_PATTERN)):
        with caminho.open(encoding='utf-8-sig', newline='') as arquivo:
            yield from csv.DictReader(arquivo)


def codigo_do_nome(nome):
    nome_normalizado = normalizar_texto(nome)
    nome_normalizado = re.sub(r'\(\s*ACAO\s+', '(', nome_normalizado)
    match = re.fullmatch(r'SUBPROJETO\s+(.+)', nome_normalizado)
    if not match:
        return None
    return extrair_codigo(match.group(1))


class Command(BaseCommand):
    help = 'Sincroniza nomes e cria projetos/subprojetos a partir dos CSVs TCCE.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--apply',
            action='store_true',
            help='Persiste as alterações. Sem esta opção, executa somente validação.',
        )

    def handle(self, *args, **options):
        base_dir = Path.cwd()
        linhas = list(carregar_linhas(base_dir))
        if not linhas:
            raise CommandError(f'Nenhum arquivo encontrado: {base_dir / CSV_PATTERN}')

        projetos = {
            normalizar_tcce(projeto.nome): projeto
            for projeto in Projeto.objects_all.all()
        }
        subprojetos_por_codigo = {}
        subprojetos_por_nome = {}
        for subprojeto in Subprojeto.objects_all.select_related('projeto'):
            chave_projeto = normalizar_tcce(subprojeto.projeto.nome)
            codigo = codigo_do_nome(subprojeto.nome)
            if codigo:
                subprojetos_por_codigo.setdefault(
                    (chave_projeto, codigo), []
                ).append(subprojeto)
            subprojetos_por_nome.setdefault(
                (chave_projeto, subprojeto.nome), []
            ).append(subprojeto)

        atualizacoes = []
        criacoes_projetos = {}
        criacoes_subprojetos = []
        duplicatas = []
        erros = []
        chaves_processadas = set()

        for linha in linhas:
            tcce = normalizar_tcce(linha['TCCE'])
            codigo = extrair_codigo(linha['Subprojeto'])
            novo_nome = linha['Nome do Projeto'].strip()
            projeto = projetos.get(tcce)

            if projeto is None:
                projeto = criacoes_projetos.setdefault(tcce, Projeto(nome=tcce, ativo=True))

            chave = (tcce, codigo)
            if chave in chaves_processadas:
                erros.append(f'Linha duplicada: {linha["TCCE"]} / {linha["Subprojeto"]}')
                continue
            chaves_processadas.add(chave)

            correspondentes_codigo = subprojetos_por_codigo.get((tcce, codigo), [])
            correspondentes_nome = subprojetos_por_nome.get((tcce, novo_nome), [])
            if len(correspondentes_codigo) > 1:
                erros.append(f'Múltiplos subprojetos para: {linha["TCCE"]} / {linha["Subprojeto"]}')
                continue
            if len(correspondentes_nome) > 1:
                erros.append(f'Múltiplos subprojetos com o nome: {linha["Nome do Projeto"]}')
                continue

            subprojeto_codigo = correspondentes_codigo[0] if correspondentes_codigo else None
            subprojeto_nome = correspondentes_nome[0] if correspondentes_nome else None
            if subprojeto_codigo and subprojeto_nome and subprojeto_codigo != subprojeto_nome:
                duplicatas.append((subprojeto_codigo, subprojeto_nome))
                atualizacoes.append((subprojeto_codigo, novo_nome))
            elif subprojeto_codigo:
                subprojeto = subprojeto_codigo
                if subprojeto.nome != novo_nome:
                    atualizacoes.append((subprojeto, novo_nome))
            elif subprojeto_nome:
                continue
            else:
                criacoes_subprojetos.append((projeto, codigo, novo_nome))

        if erros:
            raise CommandError('\n'.join(erros))

        atualizacoes_por_id = {
            subprojeto.pk: (subprojeto, novo_nome)
            for subprojeto, novo_nome in atualizacoes
        }

        self.stdout.write(
            f'{len(atualizacoes_por_id)} atualização(ões), '
            f'{len(criacoes_projetos)} projeto(s) novo(s), '
            f'{len(criacoes_subprojetos)} subprojeto(s) novo(s), '
            f'{len(duplicatas)} duplicata(s) a consolidar.'
        )

        if not options['apply']:
            self.stdout.write('Validação concluída. Use --apply para persistir.')
            return

        with transaction.atomic():
            for projeto in criacoes_projetos.values():
                projeto.save()
            for subprojeto_canonico, subprojeto_duplicado in duplicatas:
                Registro.objects_all.filter(subprojeto=subprojeto_duplicado).update(
                    subprojeto=subprojeto_canonico
                )
                subprojeto_duplicado.delete()
            for projeto, codigo, novo_nome in criacoes_subprojetos:
                Subprojeto.objects.create(projeto=projeto, nome=novo_nome, ativo=True)
            for subprojeto, novo_nome in atualizacoes_por_id.values():
                subprojeto.nome = novo_nome
            if atualizacoes_por_id:
                Subprojeto.objects_all.bulk_update(
                    [subprojeto for subprojeto, _ in atualizacoes_por_id.values()],
                    ['nome'],
                )

        self.stdout.write(self.style.SUCCESS('Sincronização concluída com sucesso.'))

import csv
import re
import unicodedata
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from apps.repositorio.models import Projeto, Subprojeto


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
    return extrair_codigo(nome.replace('SUBPROJETO', '', 1).strip())


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

        projetos = {normalizar_tcce(projeto.nome): projeto for projeto in Projeto.objects.all()}
        existentes = {}
        atualizacoes = []
        criacoes_projetos = {}
        criacoes_subprojetos = []
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

            subprojetos = list(Subprojeto.objects.filter(projeto=projeto)) if projeto.pk else []
            correspondentes = [
                subprojeto for subprojeto in subprojetos
                if codigo_do_nome(subprojeto.nome) == codigo
            ]
            if len(correspondentes) > 1:
                erros.append(f'Múltiplos subprojetos para: {linha["TCCE"]} / {linha["Subprojeto"]}')
                continue
            if correspondentes:
                subprojeto = correspondentes[0]
                existentes[chave] = subprojeto
                if subprojeto.nome != novo_nome:
                    atualizacoes.append((subprojeto, novo_nome))
            else:
                criacoes_subprojetos.append((projeto, codigo, novo_nome))

        if erros:
            raise CommandError('\n'.join(erros))

        self.stdout.write(
            f'{len(atualizacoes)} atualização(ões), '
            f'{len(criacoes_projetos)} projeto(s) novo(s), '
            f'{len(criacoes_subprojetos)} subprojeto(s) novo(s).'
        )

        if not options['apply']:
            self.stdout.write('Validação concluída. Use --apply para persistir.')
            return

        with transaction.atomic():
            for projeto in criacoes_projetos.values():
                projeto.save()
            for projeto, codigo, novo_nome in criacoes_subprojetos:
                Subprojeto.objects.create(projeto=projeto, nome=novo_nome, ativo=True)
            for subprojeto, novo_nome in atualizacoes:
                subprojeto.nome = novo_nome
                subprojeto.save(update_fields=['nome'])

        self.stdout.write(self.style.SUCCESS('Sincronização concluída com sucesso.'))

import tempfile
from pathlib import Path
from unittest.mock import patch

from django.core.management import call_command
from django.test import TestCase

from apps.accounts.models.user import User
from apps.repositorio.models.repositorio import (
    AreaTematica,
    Projeto,
    Registro,
    Status,
    Subprojeto,
    TipoDocumento,
    TipoPublicacao,
)
from apps.repositorio.management.commands.sincronizar_subprojetos_tcce import codigo_do_nome


class SincronizarSubprojetosTCCETest(TestCase):
    def test_codigo_do_nome_aceita_acao_com_e_sem_prefixo(self):
        self.assertEqual(codigo_do_nome('SUBPROJETO 22 (4.20.5)'), '22 (4.20.5)')
        self.assertEqual(
            codigo_do_nome('SUBPROJETO 22 (AÇÃO 4.20.5)'),
            '22 (4.20.5)',
        )

    def setUp(self):
        self.projeto = Projeto.objects.create(nome='TCCE 1/2018')
        self.subprojeto_legado = Subprojeto.objects.create(
            projeto=self.projeto,
            nome='SUBPROJETO 1',
        )
        self.subprojeto_duplicado = Subprojeto.objects.create(
            projeto=self.projeto,
            nome='Nome atualizado',
        )
        user = User.objects.create_user(
            email='sincronizacao@example.com',
            password='secret123',
        )
        self.registro = Registro.objects.create(
            titulo='Registro vinculado ao subprojeto duplicado',
            subprojeto=self.subprojeto_duplicado,
            tipo_documento=TipoDocumento.objects.create(nome='Artigo'),
            area_tematica=AreaTematica.objects.create(nome='Biologia'),
            status=Status.objects.create(nome='Publicado'),
            tipo_publicacao=TipoPublicacao.objects.create(nome='Revista'),
            usuario_criacao=user,
            usuario_ultima_atualizacao=user,
            link_externo='https://exemplo.test/registro',
        )
        self.registro_legado = Registro.objects.create(
            titulo='Registro vinculado ao subprojeto legado',
            subprojeto=self.subprojeto_legado,
            tipo_documento=self.registro.tipo_documento,
            area_tematica=self.registro.area_tematica,
            status=self.registro.status,
            tipo_publicacao=self.registro.tipo_publicacao,
            usuario_criacao=user,
            usuario_ultima_atualizacao=user,
            link_externo='https://exemplo.test/registro-legado',
        )

    def test_consolida_duplicata_e_renomeia_subprojeto_legado(self):
        subprojeto_id = self.subprojeto_legado.pk
        registro_legado_subprojeto_id = self.registro_legado.subprojeto_id

        with tempfile.TemporaryDirectory() as directory:
            Path(directory, 'Lista de Projetos TCCE - teste.csv').write_text(
                'TCCE,Subprojeto,Nome do Projeto\n'
                'TCCE - 1/2018,Subprojeto 01,Nome atualizado\n',
                encoding='utf-8',
            )
            with patch(
                'apps.repositorio.management.commands.sincronizar_subprojetos_tcce.Path.cwd',
                return_value=Path(directory),
            ):
                call_command('sincronizar_subprojetos_tcce', '--apply')

        self.subprojeto_legado.refresh_from_db()
        self.registro.refresh_from_db()
        self.registro_legado.refresh_from_db()

        self.assertEqual(self.subprojeto_legado.nome, 'Nome atualizado')
        self.assertEqual(self.subprojeto_legado.pk, subprojeto_id)
        self.assertEqual(self.registro.subprojeto, self.subprojeto_legado)
        self.assertEqual(self.registro_legado.subprojeto_id, registro_legado_subprojeto_id)
        self.assertEqual(self.registro_legado.subprojeto_id, self.subprojeto_legado.pk)
        self.assertFalse(Subprojeto.objects_all.filter(pk=self.subprojeto_duplicado.pk).exists())

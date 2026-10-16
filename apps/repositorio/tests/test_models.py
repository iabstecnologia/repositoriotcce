from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.accounts.models.user import User
from apps.repositorio.models.repositorio import (
    AreaTematica,
    Autor,
    Projeto,
    Registro,
    Status,
    SubAreaTematica,
    Subprojeto,
    Tag,
    TipoDocumento,
    TipoPublicacao,
)


class RegistroSpeciesFieldsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='tester@example.com',
            password='secret123',
            first_name='Tester',
            last_name='User',
        )
        self.projeto = Projeto.objects.create(nome='Projeto Teste', ativo=True)
        self.subprojeto = Subprojeto.objects.create(projeto=self.projeto, nome='Subprojeto Teste', ativo=True)
        self.tipo_documento = TipoDocumento.objects.create(nome='Artigo', ativo=True)
        self.area_tematica = AreaTematica.objects.create(nome='Biologia', ativo=True)
        self.subarea_tematica = SubAreaTematica.objects.create(
            area_tematica=self.area_tematica,
            nome='Ecologia Aplicada',
            ativo=True,
        )
        self.outra_area_tematica = AreaTematica.objects.create(nome='Geologia', ativo=True)
        self.subarea_outra_area = SubAreaTematica.objects.create(
            area_tematica=self.outra_area_tematica,
            nome='Geomorfologia',
            ativo=True,
        )
        self.status = Status.objects.create(nome='Publicado', ativo=True)
        self.tipo_publicacao = TipoPublicacao.objects.create(nome='Revista', ativo=True)
        self.autor = Autor.objects.create(nome='Autor Teste', ativo=True)
        self.tag = Tag.objects.create(nome='Tag Teste', ativo=True)

    def test_registro_maintains_species_fields_defaults(self):
        registro = Registro.objects.create(
            titulo='Registro de teste',
            subprojeto=self.subprojeto,
            tipo_documento=self.tipo_documento,
            area_tematica=self.area_tematica,
            status=self.status,
            tipo_publicacao=self.tipo_publicacao,
            usuario_criacao=self.user,
            usuario_ultima_atualizacao=self.user,
            link_externo='https://exemplo.test/registro',
        )

        registro.autores.add(self.autor)
        registro.tags.add(self.tag)

        self.assertFalse(registro.especie_nova)
        self.assertIsNone(registro.especie_informacoes)

    def test_registro_can_store_species_information(self):
        registro = Registro.objects.create(
            titulo='Registro com espécies novas',
            subprojeto=self.subprojeto,
            tipo_documento=self.tipo_documento,
            area_tematica=self.area_tematica,
            status=self.status,
            tipo_publicacao=self.tipo_publicacao,
            usuario_criacao=self.user,
            usuario_ultima_atualizacao=self.user,
            especie_nova=True,
            especie_informacoes='Rana amazonica, 3 espécimes',
            link_externo='https://exemplo.test/registro-especie',
        )

        registro.autores.add(self.autor)
        registro.tags.add(self.tag)

        self.assertTrue(registro.especie_nova)
        self.assertEqual(registro.especie_informacoes, 'Rana amazonica, 3 espécimes')

    def test_record_rejects_subarea_from_another_thematic_area(self):
        registro = Registro.objects.create(
            titulo='Registro com subárea incompatível',
            subprojeto=self.subprojeto,
            tipo_documento=self.tipo_documento,
            area_tematica=self.area_tematica,
            status=self.status,
            tipo_publicacao=self.tipo_publicacao,
            usuario_criacao=self.user,
            usuario_ultima_atualizacao=self.user,
            link_externo='https://exemplo.test/registro-invalido',
        )

        with self.assertRaises(ValidationError):
            registro.subareas_tematicas.add(self.subarea_outra_area)

    def test_subarea_rejects_record_from_another_thematic_area(self):
        registro = Registro.objects.create(
            titulo='Registro com associação inversa incompatível',
            subprojeto=self.subprojeto,
            tipo_documento=self.tipo_documento,
            area_tematica=self.area_tematica,
            status=self.status,
            tipo_publicacao=self.tipo_publicacao,
            usuario_criacao=self.user,
            usuario_ultima_atualizacao=self.user,
            link_externo='https://exemplo.test/registro-inverso-invalido',
        )

        with self.assertRaises(ValidationError):
            self.subarea_outra_area.registros.add(registro)

    def test_record_rejects_area_change_that_conflicts_with_existing_subareas(self):
        registro = Registro.objects.create(
            titulo='Registro com área alterada',
            subprojeto=self.subprojeto,
            tipo_documento=self.tipo_documento,
            area_tematica=self.area_tematica,
            status=self.status,
            tipo_publicacao=self.tipo_publicacao,
            usuario_criacao=self.user,
            usuario_ultima_atualizacao=self.user,
            link_externo='https://exemplo.test/registro-area-alterada',
        )
        registro.subareas_tematicas.add(self.subarea_tematica)
        registro.area_tematica = self.outra_area_tematica

        with self.assertRaises(ValidationError):
            registro.save()

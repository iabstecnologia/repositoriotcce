from django.test import TestCase

from apps.accounts.models.user import User
from apps.repositorio.forms.registro_form import RegistroForm
from apps.repositorio.models.repositorio import (
    AreaTematica,
    Autor,
    Projeto,
    Status,
    SubAreaTematica,
    Subprojeto,
    Tag,
    Registro,
    TipoDocumento,
    TipoPublicacao,
)


class RegistroFormSpeciesFieldsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='formtester@example.com',
            password='secret123',
            first_name='Form',
            last_name='Tester',
        )
        self.projeto = Projeto.objects.create(nome='Projeto Form', ativo=True)
        self.subprojeto = Subprojeto.objects.create(projeto=self.projeto, nome='Subprojeto Form', ativo=True)
        self.tipo_documento = TipoDocumento.objects.create(nome='Relatório', ativo=True)
        self.area_tematica = AreaTematica.objects.create(nome='Ecologia', ativo=True)
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
        self.status = Status.objects.create(nome='Em Revisão', ativo=True, is_public=False)
        self.tipo_publicacao = TipoPublicacao.objects.create(nome='Anais', ativo=True)
        self.autor = Autor.objects.create(nome='Autor do Form', ativo=True)
        self.tag = Tag.objects.create(nome='Tag do Form', ativo=True)

    def test_form_accepts_species_fields(self):
        form = RegistroForm(data={
            'titulo': 'Registro com espécie nova',
            'subprojeto': self.subprojeto.pk,
            'autores': [self.autor.pk],
            'tags': [self.tag.pk],
            'tipo_documento': self.tipo_documento.pk,
            'area_tematica': self.area_tematica.pk,
            'subareas_tematicas': [self.subarea_tematica.pk],
            'status': self.status.pk,
            'tipo_publicacao': self.tipo_publicacao.pk,
            'data_publicacao': '2026-05-27',
            'isbn': '',
            'link_externo': 'https://exemplo.test/registro-form',
            'especie_nova': 'on',
            'especie_informacoes': 'Rana sp., 5 espécimes',
            'ativo': 'on',
        })

        self.assertTrue(form.is_valid(), form.errors)
        self.assertTrue(form.cleaned_data['especie_nova'])
        self.assertEqual(form.cleaned_data['especie_informacoes'], 'Rana sp., 5 espécimes')

    def test_form_rejects_subarea_from_another_thematic_area(self):
        form = RegistroForm(data={
            'titulo': 'Registro com subárea incompatível',
            'subprojeto': self.subprojeto.pk,
            'autores': [self.autor.pk],
            'tags': [self.tag.pk],
            'tipo_documento': self.tipo_documento.pk,
            'area_tematica': self.area_tematica.pk,
            'subareas_tematicas': [self.subarea_outra_area.pk],
            'status': self.status.pk,
            'tipo_publicacao': self.tipo_publicacao.pk,
            'link_externo': 'https://exemplo.test/registro-form-invalido',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('subareas_tematicas', form.errors)

    def test_form_can_change_area_and_replace_subareas(self):
        registro = Registro.objects.create(
            titulo='Registro a reclassificar',
            subprojeto=self.subprojeto,
            tipo_documento=self.tipo_documento,
            area_tematica=self.area_tematica,
            status=self.status,
            tipo_publicacao=self.tipo_publicacao,
            usuario_criacao=self.user,
            usuario_ultima_atualizacao=self.user,
            link_externo='https://exemplo.test/registro-reclassificar',
        )
        registro.autores.add(self.autor)
        registro.tags.add(self.tag)
        registro.subareas_tematicas.add(self.subarea_tematica)

        form = RegistroForm(
            data={
                'titulo': registro.titulo,
                'subprojeto': self.subprojeto.pk,
                'autores': [self.autor.pk],
                'tags': [self.tag.pk],
                'tipo_documento': self.tipo_documento.pk,
                'area_tematica': self.outra_area_tematica.pk,
                'subareas_tematicas': [self.subarea_outra_area.pk],
                'status': self.status.pk,
                'tipo_publicacao': self.tipo_publicacao.pk,
                'link_externo': registro.link_externo,
            },
            instance=registro,
        )

        self.assertTrue(form.is_valid(), form.errors)
        registro_atualizado = form.save()

        self.assertEqual(registro_atualizado.area_tematica, self.outra_area_tematica)
        self.assertEqual(
            list(registro_atualizado.subareas_tematicas.all()),
            [self.subarea_outra_area],
        )

from django.test import TestCase

from apps.accounts.models.user import User
from apps.repositorio.forms.registro_form import RegistroForm
from apps.repositorio.models.repositorio import (
    AreaTematica,
    Autor,
    Projeto,
    Status,
    Subprojeto,
    Tag,
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

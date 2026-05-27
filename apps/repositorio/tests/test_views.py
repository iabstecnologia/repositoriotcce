from django.test import TestCase
from django.urls import reverse

from apps.accounts.models.user import User
from apps.repositorio.models.repositorio import (
    AreaTematica,
    Autor,
    Projeto,
    Registro,
    Status,
    Subprojeto,
    Tag,
    TipoDocumento,
    TipoPublicacao,
)


class RegistroCreateViewSpeciesFieldsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='viewtester@example.com',
            password='secret123',
            first_name='View',
            last_name='Tester',
        )
        self.projeto = Projeto.objects.create(nome='Projeto View', ativo=True)
        self.subprojeto = Subprojeto.objects.create(projeto=self.projeto, nome='Subprojeto View', ativo=True)
        self.tipo_documento = TipoDocumento.objects.create(nome='Documento', ativo=True)
        self.area_tematica = AreaTematica.objects.create(nome='Zoologia', ativo=True)
        self.status = Status.objects.create(nome='Rascunho', ativo=True, is_public=False)
        self.tipo_publicacao = TipoPublicacao.objects.create(nome='Livro', ativo=True)
        self.autor = Autor.objects.create(nome='Autor da View', ativo=True)
        self.tag = Tag.objects.create(nome='Tag da View', ativo=True)

    def test_create_view_renders_species_fields(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('repositorio:criar'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Registro relacionado a espécies novas?')
        self.assertContains(response, 'Nome científico e/ou quantidade')

    def test_create_view_persists_species_fields(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse('repositorio:criar'),
            {
                'titulo': 'Registro criado por teste',
                'subprojeto': self.subprojeto.pk,
                'autores': [self.autor.pk],
                'tags': [self.tag.pk],
                'tipo_documento': self.tipo_documento.pk,
                'area_tematica': self.area_tematica.pk,
                'status': self.status.pk,
                'tipo_publicacao': self.tipo_publicacao.pk,
                'data_publicacao': '2026-05-27',
                'link_externo': 'https://exemplo.test/registro-view',
                'especie_nova': 'on',
                'especie_informacoes': 'Rana sp., 7 espécimes',
                'ativo': 'on',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Registro.objects.filter(especie_nova=True, especie_informacoes='Rana sp., 7 espécimes').exists())

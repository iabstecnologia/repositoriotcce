from django.test import TestCase
from django.urls import reverse

from apps.accounts.models.user import User
from apps.core.views.website import TCCEView
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
        self.subarea_tematica = SubAreaTematica.objects.create(
            area_tematica=self.area_tematica,
            nome='Zoologia Aplicada',
            ativo=True,
        )
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
                'subareas_tematicas': [self.subarea_tematica.pk],
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


class TCCEViewCountersTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='countertester@example.com',
            password='secret123',
            first_name='Counter',
            last_name='Tester',
        )
        self.projeto = Projeto.objects.create(pk=1, nome='TCCE 1/2018', ativo=True)
        self.subprojeto = Subprojeto.objects.create(
            projeto=self.projeto,
            nome='Subprojeto ativo',
            ativo=True,
        )
        self.subprojeto_inativo = Subprojeto.objects.create(
            projeto=self.projeto,
            nome='Subprojeto inativo',
            ativo=False,
        )
        self.projeto_inativo = Projeto.objects.create(pk=2, nome='TCCE inativo', ativo=False)
        self.subprojeto_projeto_inativo = Subprojeto.objects.create(
            projeto=self.projeto_inativo,
            nome='Subprojeto de projeto inativo',
            ativo=True,
        )
        self.artigo = TipoDocumento.objects.create(nome='ARTIGO CIENTÍFICO', ativo=True)
        self.relatorio = TipoDocumento.objects.create(nome='RELATÓRIO TÉCNICO FINAL', ativo=True)
        self.status_publicado = Status.objects.create(nome='PUBLICADO', ativo=True, is_public=True)
        self.status_rascunho = Status.objects.create(nome='RASCUNHO', ativo=True, is_public=False)
        self.tipo_publicacao = TipoPublicacao.objects.create(nome='Revista', ativo=True)
        self.area_tematica = AreaTematica.objects.create(nome='Biologia', ativo=True)
        self.tag = Tag.objects.create(nome='Contadores', ativo=True)
        self.autor_ativo = Autor.objects.create(nome='Autor ativo', ativo=True)
        self.autor_inativo = Autor.objects.create(nome='Autor inativo', ativo=False)

    def _criar_registro(self, *, subprojeto, tipo_documento, status, ativo=True):
        registro = Registro.objects.create(
            titulo=f'Registro {Registro.objects_all.count() + 1}',
            subprojeto=subprojeto,
            tipo_documento=tipo_documento,
            area_tematica=self.area_tematica,
            status=status,
            tipo_publicacao=self.tipo_publicacao,
            usuario_criacao=self.user,
            usuario_ultima_atualizacao=self.user,
            link_externo='https://exemplo.test/contador',
            ativo=ativo,
        )
        registro.tags.add(self.tag)
        return registro

    def test_counters_match_active_objects_in_database(self):
        registro_artigo = self._criar_registro(
            subprojeto=self.subprojeto,
            tipo_documento=self.artigo,
            status=self.status_publicado,
        )
        registro_artigo.autores.add(self.autor_ativo, self.autor_inativo)
        registro_relatorio = self._criar_registro(
            subprojeto=self.subprojeto,
            tipo_documento=self.relatorio,
            status=self.status_rascunho,
        )
        registro_relatorio.autores.add(self.autor_ativo)
        registro_inativo = self._criar_registro(
            subprojeto=self.subprojeto,
            tipo_documento=self.artigo,
            status=self.status_publicado,
            ativo=False,
        )
        registro_inativo.autores.add(Autor.objects.create(nome='Autor de registro inativo', ativo=True))
        registro_subprojeto_inativo = self._criar_registro(
            subprojeto=self.subprojeto_inativo,
            tipo_documento=self.relatorio,
            status=self.status_publicado,
        )
        registro_subprojeto_inativo.autores.add(Autor.objects.create(nome='Autor de subprojeto inativo', ativo=True))
        registro_projeto_inativo = self._criar_registro(
            subprojeto=self.subprojeto_projeto_inativo,
            tipo_documento=self.artigo,
            status=self.status_publicado,
        )
        registro_projeto_inativo.autores.add(Autor.objects.create(nome='Autor de projeto inativo', ativo=True))

        estatisticas = TCCEView()._calcular_estatisticas_tcce(self.projeto.pk)
        estatisticas_globais = TCCEView()._calcular_estatisticas_todos_tcces()
        esperado = {
            'producoes_academicas': 2,
            'producoes_publicadas': 1,
            'artigos_cientificos': 1,
            'autores_unicos': Autor.objects.filter(
                autores__ativo=True,
                autores__subprojeto__projeto=self.projeto,
                autores__subprojeto__ativo=True,
            ).distinct().count(),
            'relatorios_tecnicos': 1,
        }

        self.assertEqual(estatisticas['autores_unicos'], 1)
        self.assertEqual(estatisticas, esperado)
        self.assertEqual(estatisticas_globais, esperado)

    def test_home_counters_match_active_projects_in_database(self):
        Projeto.objects.create(pk=3, nome='Outro TCCE ativo', ativo=True)
        Subprojeto.objects.create(
            projeto=self.projeto,
            nome='Outro subprojeto ativo',
            ativo=True,
        )
        Projeto.objects.create(pk=4, nome='Outro TCCE inativo', ativo=False)
        Subprojeto.objects.create(
            projeto=self.projeto_inativo,
            nome='Subprojeto de TCCE inativo',
            ativo=True,
        )
        Subprojeto.objects.create(
            projeto=self.projeto,
            nome='Outro subprojeto inativo',
            ativo=False,
        )

        response = self.client.get(reverse('core:home'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['home_counters'], {
            'tcces_formalizados': Projeto.objects.count(),
            'projetos': Subprojeto.objects.filter(projeto__ativo=True).count(),
        })
        self.assertContains(response, 'data-target="2"')

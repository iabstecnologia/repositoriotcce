from django.test import TestCase
from django.urls import reverse

from apps.accounts.models.user import User
from apps.core.repository_filters import filter_repository_queryset
from apps.repositorio.models.repositorio import (
    AreaTematica,
    Projeto,
    Registro,
    Status,
    Subprojeto,
    TipoDocumento,
    TipoPublicacao,
)


class PublicacoesCientificasCategoryTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='categorytester@example.com',
            password='secret123',
            first_name='Category',
            last_name='Tester',
        )
        self.projeto = Projeto.objects.create(nome='Projeto de teste', ativo=True)
        self.subprojeto = Subprojeto.objects.create(
            projeto=self.projeto,
            nome='Subprojeto de teste',
            ativo=True,
        )
        self.area_tematica = AreaTematica.objects.create(nome='Biologia', ativo=True)
        self.status = Status.objects.create(nome='Publicado', ativo=True, is_public=True)
        self.tipo_publicacao = TipoPublicacao.objects.create(nome='Revista', ativo=True)

    def _criar_registro(self, tipo_documento_nome):
        tipo_documento, _ = TipoDocumento.objects.get_or_create(
            nome=tipo_documento_nome,
            defaults={'ativo': True},
        )
        return Registro.objects.create(
            titulo=f'Registro {tipo_documento_nome}',
            subprojeto=self.subprojeto,
            tipo_documento=tipo_documento,
            area_tematica=self.area_tematica,
            status=self.status,
            tipo_publicacao=self.tipo_publicacao,
            usuario_criacao=self.user,
            usuario_ultima_atualizacao=self.user,
            link_externo='https://exemplo.test/registro',
        )

    def test_category_filters_only_the_three_academic_document_types(self):
        elegiveis = {
            'TCC/MONOGRAFIA': self._criar_registro('TCC/MONOGRAFIA'),
            'TESE': self._criar_registro('TESE'),
            'DISSERTAÇÃO': self._criar_registro('DISSERTAÇÃO'),
        }
        self._criar_registro('ARTIGO CIENTÍFICO')
        self._criar_registro('ANAIS DE EVENTOS')

        resultado = filter_repository_queryset({'categoria': 'publicacoes_cientificas'})

        self.assertSetEqual(
            set(resultado.values_list('pk', flat=True)),
            {registro.pk for registro in elegiveis.values()},
        )

    def test_oldest_first_ordering_is_applied(self):
        recente = self._criar_registro('LIVRO')
        antigo = self._criar_registro('TESE')
        Registro.objects.filter(pk=recente.pk).update(data_publicacao='2024-01-01')
        Registro.objects.filter(pk=antigo.pk).update(data_publicacao='2020-01-01')

        resultado = filter_repository_queryset({'ordenar_por': 'data_publicacao'})

        self.assertEqual(list(resultado.values_list('pk', flat=True)), [antigo.pk, recente.pk])

    def test_non_numeric_ids_return_no_records_instead_of_failing(self):
        self._criar_registro('LIVRO')

        for campo in ('projeto', 'subprojeto', 'autor', 'tag', 'area_tematica', 'subarea_tematica', 'status'):
            with self.subTest(campo=campo):
                resultado = filter_repository_queryset({campo: 'abc'})

                self.assertFalse(resultado.exists())

    def test_explicit_category_filters_only_its_configured_document_type(self):
        artigo_cientifico = self._criar_registro('ARTIGO CIENTÍFICO')
        self._criar_registro('ARTIGO DE OPINIÃO')

        resultado = filter_repository_queryset({'categoria': 'artigos'})

        self.assertSetEqual(
            set(resultado.values_list('pk', flat=True)),
            {artigo_cientifico.pk},
        )

    def test_category_matching_is_case_insensitive(self):
        artigo = self._criar_registro('artigo científico')

        resultado = filter_repository_queryset({'categoria': 'ARTIGOS'})
        response = self.client.get(reverse('core:repositorio'))

        self.assertSetEqual(
            set(resultado.values_list('pk', flat=True)),
            {artigo.pk},
        )
        self.assertContains(response, '?categoria=artigos')

    def test_other_category_slugs_match_only_their_configured_types(self):
        registros_por_categoria = {
            'livros': self._criar_registro('LIVRO'),
            'relatorios_tecnicos': self._criar_registro('RELATÓRIO TÉCNICO'),
            'videos': self._criar_registro('VÍDEO'),
        }

        for categoria, registro in registros_por_categoria.items():
            with self.subTest(categoria=categoria):
                resultado = filter_repository_queryset({'categoria': categoria})

                self.assertSetEqual(
                    set(resultado.values_list('pk', flat=True)),
                    {registro.pk},
                )

    def test_unknown_category_returns_no_records(self):
        self._criar_registro('ARTIGO CIENTÍFICO')

        resultado = filter_repository_queryset({'categoria': 'anais'})

        self.assertFalse(resultado.exists())

    def test_category_excludes_records_of_inactive_document_types(self):
        ativos = {
            'TCC/MONOGRAFIA': self._criar_registro('TCC/MONOGRAFIA'),
            'TESE': self._criar_registro('TESE'),
            'DISSERTAÇÃO': self._criar_registro('DISSERTAÇÃO'),
        }

        for tipo_nome in ('TCC/MONOGRAFIA', 'DISSERTAÇÃO'):
            TipoDocumento.objects_all.filter(nome=tipo_nome).update(ativo=False)

        resultado = filter_repository_queryset({'categoria': 'publicacoes_cientificas'})

        self.assertSetEqual(
            set(resultado.values_list('pk', flat=True)),
            {ativos['TESE'].pk},
        )

        TipoDocumento.objects_all.update(ativo=False)
        resultado_sem_tipos_ativos = filter_repository_queryset(
            {'categoria': 'publicacoes_cientificas'}
        )

        self.assertFalse(resultado_sem_tipos_ativos.exists())

    def test_category_card_is_unavailable_when_no_matching_document_type_exists(self):
        response = self.client.get(reverse('core:repositorio'))

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, '?categoria=publicacoes_cientificas')
        self.assertContains(response, 'title="Categoria indisponível"')

    def test_category_card_links_to_filtered_search_when_a_matching_type_exists(self):
        tipos_documento = {
            nome: TipoDocumento.objects.create(nome=nome, ativo=True)
            for nome in ('TCC/MONOGRAFIA', 'TESE', 'DISSERTAÇÃO')
        }
        TipoDocumento.objects_all.filter(
            pk__in=[tipos_documento['TCC/MONOGRAFIA'].pk, tipos_documento['DISSERTAÇÃO'].pk]
        ).update(ativo=False)

        response = self.client.get(reverse('core:repositorio'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '?categoria=publicacoes_cientificas')

    def test_category_card_is_unavailable_when_all_matching_types_are_inactive(self):
        for tipo_nome in ('TCC/MONOGRAFIA', 'TESE', 'DISSERTAÇÃO'):
            TipoDocumento.objects_all.create(nome=tipo_nome, ativo=False)

        response = self.client.get(reverse('core:repositorio'))

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, '?categoria=publicacoes_cientificas')
        self.assertContains(response, 'title="Categoria indisponível"')

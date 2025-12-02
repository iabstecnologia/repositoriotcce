from django.views.generic import ListView
from django.db.models import Q
from django.shortcuts import render
from datetime import datetime
from apps.repositorio.models.repositorio import Registro
from apps.core.forms import RepositorioFilterForm


class RepositorioView(ListView):
    """
    Lista todos os Registros (Documentos) e gerencia a pesquisa avançada e filtros.
    """
    model = Registro
    template_name = 'website/repo_busca.html'
    context_object_name = 'registros'
    paginate_by = 10

    def get_queryset(self):
        """
        Retorna o queryset base (apenas documentos ativos e públicos) e aplica os filtros
        recebidos via GET.
        """
        # Filtro base: Apenas registros ativos e com status público
        queryset = Registro.objects.filter(
            ativo=True,
            status__is_public=True
        ).prefetch_related(
            'autores', 'tags', 'subprojeto__projeto'  # Otimiza o carregamento de FKs e M2M
        )

        # Obtém os parâmetros de busca da URL
        query = self.request.GET.get('q')
        subprojeto_id = self.request.GET.get('subprojeto')
        autor_id = self.request.GET.get('autor')
        tag_id = self.request.GET.get('tag')
        tipo_documento_id = self.request.GET.get('tipo_documento')
        area_tematica_id = self.request.GET.get('area_tematica')
        status_id = self.request.GET.get('status')
        tipo_publicacao_id = self.request.GET.get('tipo_publicacao')
        ano = self.request.GET.get('ano')
        ordenar_por = self.request.GET.get('ordenar_por', '-data_publicacao')

        # --- LÓGICA DE FILTRAGEM ---

        # 1. Filtro Full-Text (Título, Resumo, Tags, etc.)
        if query:
            # Usando Q objects para construir uma cláusula OR (busca em múltiplos campos)
            queryset = queryset.filter(
                Q(titulo__icontains=query) |
                Q(resumo__icontains=query) |
                Q(autores__nome__icontains=query) |
                Q(tags__nome__icontains=query)
            ).distinct()  # Necessário devido à busca M2M (autores, tags)

        # 2. Filtros de Seleção (FKs e M2M)
        if subprojeto_id:
            queryset = queryset.filter(subprojeto__id=subprojeto_id)
        if autor_id:
            queryset = queryset.filter(autores__id=autor_id)
        if tag_id:
            queryset = queryset.filter(tags__id=tag_id)
        if tipo_documento_id:
            queryset = queryset.filter(tipo_documento__id=tipo_documento_id)
        if area_tematica_id:
            queryset = queryset.filter(area_tematica__id=area_tematica_id)
        if status_id:
            queryset = queryset.filter(status__id=status_id)
        if tipo_publicacao_id:
            queryset = queryset = queryset.filter(tipo_publicacao__id=tipo_publicacao_id)

        # 3. Filtro por Ano
        if ano:
            try:
                ano = int(ano)
                # Filtra pela data_publicacao__year
                queryset = queryset.filter(data_publicacao__year=ano)
            except ValueError:
                pass  # Ignora se o ano for inválido

        # 4. Ordenação
        if ordenar_por:
            queryset = queryset.order_by(ordenar_por)

        return queryset

    def get_context_data(self, **kwargs):
        """
        Adiciona o formulário de filtro e os dados de contexto ao template.
        """
        context = super().get_context_data(**kwargs)

        # Instancia o formulário de filtro, preenchendo-o com os dados da requisição (GET)
        context['form'] = RepositorioFilterForm(self.request.GET)

        # Se for necessário passar o termo de busca para o campo de busca simples no Header
        context['search_term'] = self.request.GET.get('q', '')

        return context
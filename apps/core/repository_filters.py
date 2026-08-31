from datetime import datetime

from django.db.models import Q

from apps.core.forms.repositorio import RepositorioFilterForm
from apps.repositorio.models.repositorio import Registro, TipoDocumento


def filter_repository_queryset(query_params):
    """Aplica os filtros públicos de busca ao queryset de registros."""
    queryset = Registro.objects.filter(
        ativo=True,
        status__is_public=True
    ).prefetch_related(
        'autores',
        'tags',
        'subprojeto__projeto',
        'subareas_tematicas__area_tematica',
    )

    query = query_params.get('q')
    projeto_id = query_params.get('projeto')
    subprojeto_id = query_params.get('subprojeto')
    autor_id = query_params.get('autor')
    tag_id = query_params.get('tag')
    tipo_documento_id = query_params.get('tipo_documento')
    categoria = query_params.get('categoria')
    area_tematica_id = query_params.get('area_tematica')
    subarea_tematica_id = query_params.get('subarea_tematica') or query_params.get('subareas_tematicas')
    status_id = query_params.get('status')
    ano = query_params.get('ano')
    ordenar_por = query_params.get('ordenar_por', '-data_publicacao')

    if query:
        queryset = queryset.filter(
            Q(titulo__icontains=query) |
            Q(resumo__icontains=query) |
            Q(autores__nome__icontains=query) |
            Q(tags__nome__icontains=query)
        ).distinct()

    if projeto_id:
        queryset = queryset.filter(subprojeto__projeto_id=projeto_id)
    if subprojeto_id:
        queryset = queryset.filter(subprojeto__id=subprojeto_id)
    if autor_id:
        queryset = queryset.filter(autores__id=autor_id)
    if tag_id:
        queryset = queryset.filter(tags__id=tag_id)
    if tipo_documento_id:
        if str(tipo_documento_id).isdigit():
            queryset = queryset.filter(tipo_documento__id=tipo_documento_id)
        else:
            queryset = queryset.filter(tipo_documento__nome__icontains=tipo_documento_id)

    if categoria:
        norm = categoria.strip()
        if len(norm) > 1 and (norm.endswith('s') or norm.endswith('S')):
            norm = norm[:-1]
        norm = (norm
                .replace('í', 'i').replace('Í', 'I')
                .replace('é', 'e').replace('É', 'E')
                .replace('á', 'a').replace('Á', 'A')
                .replace('ó', 'o').replace('Ó', 'O')
                .replace('ú', 'u').replace('Ú', 'U')
                .replace('ã', 'a').replace('Ã', 'A')
                .replace('õ', 'o').replace('Õ', 'O'))
        queryset = queryset.filter(tipo_documento__nome__icontains=norm)

    if area_tematica_id:
        queryset = queryset.filter(area_tematica__id=area_tematica_id)
    if subarea_tematica_id:
        queryset = queryset.filter(subareas_tematicas__id=subarea_tematica_id).distinct()
    if status_id:
        queryset = queryset.filter(status__id=status_id)

    if ano:
        try:
            ano = int(ano)
            queryset = queryset.filter(data_publicacao__year=ano)
        except ValueError:
            pass

    if ordenar_por:
        queryset = queryset.order_by(ordenar_por)

    return queryset


def build_repositorio_filter_context(query_params):
    """Prepara o contexto público de busca avançada para o template."""
    form = RepositorioFilterForm(query_params)
    search_term = query_params.get('q', '')

    tipos_documento = TipoDocumento.objects.all().order_by('nome')
    category_mapping = {
        'Livros': tipos_documento.filter(nome__icontains='LIVRO').first(),
        'Artigos': tipos_documento.filter(nome__icontains='ARTIGO').first(),
        'RelatórioTécnico': tipos_documento.filter(nome__icontains='RELATÓRIO').first(),
        'Vídeos': tipos_documento.filter(nome__icontains='VÍDEO').first(),
        'PublicacaoCientifica': tipos_documento.filter(nome__icontains='TRABALHOS ACADÊMICOS').first(),
    }
    category_mapping = {k: v.id for k, v in category_mapping.items() if v}

    return {
        'form': form,
        'search_term': search_term,
        'tipos_documento': tipos_documento,
        'category_mapping': category_mapping,
    }

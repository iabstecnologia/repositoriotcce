from datetime import datetime

from django.db.models import Q
from django.db.models.functions import Lower

from apps.core.forms.repositorio import RepositorioFilterForm
from apps.repositorio.models.repositorio import Registro, TipoDocumento


CATEGORIA_TIPOS_DOCUMENTO = {
    'livros': ('livro', 'capítulo de livro'),
    'artigos': ('artigo científico'),
    'relatorios_tecnicos': ('relatório técnico', 'relatório técnico final'),
    'videos': ('vídeo', 'vídeos'),
    'publicacoes_cientificas': ('tcc/monografia', 'tese', 'dissertação'),
    'publicacoes_eventos': ('publicação em eventos'),
    'materiais_educativos': ('material educativo',),
}

ORDENACOES_PERMITIDAS = frozenset({'-data_publicacao', 'data_publicacao', 'titulo'})
ORDENACAO_PADRAO = '-data_publicacao'

ANO_MINIMO = 1900


def _get_int(value):
    """Converte string em int, devolvendo None se inválido."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _filtrar_por_id(queryset, lookup, value):
    if not value:
        return queryset
    id_int = _get_int(value)
    if id_int is None:
        return queryset.none()
    return queryset.filter(**{lookup: id_int})


def _filtrar_por_texto(queryset, query):
    if not query:
        return queryset
    return queryset.filter(
        Q(titulo__icontains=query) |
        Q(resumo__icontains=query) |
        Q(autores__nome__icontains=query) |
        Q(tags__nome__icontains=query)
    )


def _filtrar_por_tipo_documento(queryset, tipo_documento):
    if not tipo_documento:
        return queryset
    queryset = queryset.filter(tipo_documento__ativo=True)
    tipo_id = _get_int(tipo_documento)
    if tipo_id is not None:
        return queryset.filter(tipo_documento__id=tipo_id)
    return queryset.filter(tipo_documento__nome__icontains=tipo_documento)


def _filtrar_por_categoria(queryset, categoria):
    if not categoria:
        return queryset

    tipos = CATEGORIA_TIPOS_DOCUMENTO.get(categoria)
    if tipos is None:
        return queryset.none()

    return queryset.filter(tipo_documento__ativo=True).annotate(
        tipo_documento_nome_normalizado=Lower('tipo_documento__nome'),
    ).filter(tipo_documento_nome_normalizado__in=tipos)


def _filtrar_por_ano(queryset, ano):
    ano_int = _get_int(ano)
    if ano_int is None:
        return queryset
    if not (ANO_MINIMO <= ano_int <= datetime.now().year):
        return queryset
    return queryset.filter(data_publicacao__year=ano_int)


def filter_repository_queryset(query_params):
    """Aplica os filtros públicos de busca ao queryset de registros."""
    queryset = Registro.objects.filter(
        ativo=True,
    ).prefetch_related(
        'autores',
        'tags',
        'subprojeto__projeto',
        'subareas_tematicas__area_tematica',
    )

    query = (query_params.get('q') or '').strip()
    projeto_id = query_params.get('projeto')
    subprojeto_id = query_params.get('subprojeto')
    autor_id = query_params.get('autor')
    tag_id = query_params.get('tag')
    tipo_documento_id = query_params.get('tipo_documento')
    categoria = (query_params.get('categoria') or '').strip().lower()
    area_tematica_id = query_params.get('area_tematica')
    subarea_tematica_id = query_params.get('subarea_tematica')
    status_id = query_params.get('status')
    ano = query_params.get('ano')
    ordenar_por = query_params.get('ordenar_por')
    if ordenar_por not in ORDENACOES_PERMITIDAS:
        ordenar_por = ORDENACAO_PADRAO

    # Filtros relacionais simples
    queryset = _filtrar_por_id(queryset, 'subprojeto__projeto_id', projeto_id)
    queryset = _filtrar_por_id(queryset, 'subprojeto__id', subprojeto_id)
    queryset = _filtrar_por_id(queryset, 'autores__id', autor_id)
    queryset = _filtrar_por_id(queryset, 'tags__id', tag_id)

    # Filtros com lógica própria
    queryset = _filtrar_por_texto(queryset, query)
    queryset = _filtrar_por_tipo_documento(queryset, tipo_documento_id)
    queryset = _filtrar_por_categoria(queryset, categoria)

    queryset = _filtrar_por_id(queryset, 'area_tematica__id', area_tematica_id)
    queryset = _filtrar_por_id(queryset, 'subareas_tematicas__id', subarea_tematica_id)
    queryset = _filtrar_por_id(queryset, 'status__id', status_id)

    queryset = _filtrar_por_ano(queryset, ano)

    # distinct apenas se algum filtro M2M pode ter duplicado
    if query or subarea_tematica_id:
        queryset = queryset.distinct()

    return queryset.order_by(ordenar_por)


def build_repositorio_filter_context(query_params):
    """Prepara o contexto público de busca avançada para o template."""
    form = RepositorioFilterForm(query_params)
    search_term = (query_params.get('q') or '').strip()

    # Materializa em lista: uma única query no banco
    tipos_documento = list(TipoDocumento.objects.order_by('nome'))
    tipos_por_nome = {t.nome.lower(): t.id for t in tipos_documento}

    category_mapping = {}
    for slug, nomes in CATEGORIA_TIPOS_DOCUMENTO.items():
        for nome in nomes:
            tipo_id = tipos_por_nome.get(nome)
            if tipo_id is not None:
                category_mapping[slug] = tipo_id
                break

    return {
        'form': form,
        'search_term': search_term,
        'tipos_documento': tipos_documento,
        'category_mapping': category_mapping,
    }
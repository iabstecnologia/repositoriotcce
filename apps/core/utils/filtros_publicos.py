"""
Helpers para popular filtros avançados da área pública.
Retorna apenas metadados que possuem pelo menos um Registro público vinculado.
"""
from django.db.models import Exists, OuterRef

from apps.repositorio.models.repositorio import (
    Registro,
    Projeto,
    Subprojeto,
    Autor,
    Tag,
    TipoDocumento,
    AreaTematica,
    SubAreaTematica,
    TipoPublicacao,
    Status,
)


def _registros_publicos():
    """
    Queryset base de registros visíveis ao público.
    Ajuste conforme a regra do seu projeto (ex: status__is_public=True).
    """
    return Registro.objects.filter(
        ativo=True,
    )


def projetos_em_uso():
    return (
        Projeto.objects.filter(ativo=True)
        .filter(Exists(_registros_publicos().filter(subprojeto__projeto=OuterRef('pk'))))
        .order_by('nome')
    )


def subprojetos_em_uso(projeto_id=None):
    qs = (
        Subprojeto.objects.filter(ativo=True)
        .filter(Exists(_registros_publicos().filter(subprojeto=OuterRef('pk'))))
        .order_by('nome')
    )
    if projeto_id:
        qs = qs.filter(projeto_id=projeto_id)
    return qs


def tipos_documento_em_uso():
    return (
        TipoDocumento.objects.filter(ativo=True)
        .filter(Exists(_registros_publicos().filter(tipo_documento=OuterRef('pk'))))
        .order_by('nome')
    )


def areas_tematicas_em_uso():
    return (
        AreaTematica.objects.filter(ativo=True)
        .filter(Exists(_registros_publicos().filter(area_tematica=OuterRef('pk'))))
        .order_by('nome')
    )


def subareas_tematicas_em_uso():
    return (
        SubAreaTematica.objects.filter(ativo=True)
        .filter(Exists(_registros_publicos().filter(subareas_tematicas=OuterRef('pk'))))
        .order_by('nome')
    )


def tipos_publicacao_em_uso():
    return (
        TipoPublicacao.objects.filter(ativo=True)
        .filter(Exists(_registros_publicos().filter(tipo_publicacao=OuterRef('pk'))))
        .order_by('nome')
    )


def status_em_uso():
    return (
        Status.objects.filter(ativo=True, is_public=True)
        .filter(Exists(_registros_publicos().filter(status=OuterRef('pk'))))
        .order_by('nome')
    )


def autores_em_uso():
    return (
        Autor.objects.filter(ativo=True)
        .filter(Exists(_registros_publicos().filter(autores=OuterRef('pk'))))
        .order_by('nome')
    )


def tags_em_uso():
    return (
        Tag.objects.filter(ativo=True)
        .filter(Exists(_registros_publicos().filter(tags=OuterRef('pk'))))
        .order_by('nome')
    )


def anos_em_uso():
    return (
        _registros_publicos()
        .exclude(data_publicacao__isnull=True)
        .values_list('data_publicacao__year', flat=True)
        .distinct()
        .order_by('-data_publicacao__year')
    )
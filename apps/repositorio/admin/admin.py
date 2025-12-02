from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from ..models.repositorio import (
    Projeto, Subprojeto, Autor, Tag, TipoDocumento,
    AreaTematica, Status, TipoPublicacao, Registro
)


# ====================================================================
# CLASSE BASE PARA METADADOS SIMPLES (DRY)
# ====================================================================

class BaseMetadataAdmin(admin.ModelAdmin):
    """Classe base para modelos auxiliares simples (nome, ativo)."""
    list_display = ('nome', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome',)
    ordering = ('nome',)
    actions = ['marcar_como_ativo', 'marcar_como_inativo']

    def marcar_como_ativo(self, request, queryset):
        queryset.update(ativo=True)
    marcar_como_ativo.short_description = "Marcar selecionados como ativos"

    def marcar_como_inativo(self, request, queryset):
        queryset.update(ativo=False)
    marcar_como_inativo.short_description = "Marcar selecionados como inativos"

# ====================================================================
# REGISTRO DOS MODELOS AUXILIARES
# ====================================================================

@admin.register(Projeto)
class ProjetoAdmin(BaseMetadataAdmin):
    """Gerenciamento de Projetos/Coleções Principais."""
    pass

@admin.register(Autor)
class AutorAdmin(BaseMetadataAdmin):
    """Gerenciamento de Autores, com campo para ID Lattes."""
    list_display = ('nome', 'lattes_id', 'ativo')
    search_fields = ('nome', 'lattes_id')
    ordering = ('nome',)

@admin.register(Tag)
class TagAdmin(BaseMetadataAdmin):
    """Gerenciamento de Palavras-chave."""
    pass

@admin.register(TipoDocumento)
class TipoDocumentoAdmin(BaseMetadataAdmin):
    """Gerenciamento de Tipos de Documentos."""
    pass

@admin.register(AreaTematica)
class AreaTematicaAdmin(BaseMetadataAdmin):
    """Gerenciamento de Áreas Temáticas."""
    pass

@admin.register(TipoPublicacao)
class TipoPublicacaoAdmin(BaseMetadataAdmin):
    """Gerenciamento de Tipos de Publicação."""
    pass

@admin.register(Status)
class StatusAdmin(BaseMetadataAdmin):
    """Gerenciamento de Status de Workflow, com indicador de acesso público."""
    list_display = ('nome', 'is_public', 'ativo')
    list_filter = ('is_public', 'ativo')
    ordering = ('nome',)

@admin.register(Subprojeto)
class SubprojetoAdmin(BaseMetadataAdmin):
    """Gerenciamento de Subprojetos, relacionado ao Projeto pai."""
    list_display = ('nome', 'projeto', 'ativo')
    list_filter = ('projeto', 'ativo')
    search_fields = ('nome', 'projeto__nome')
    ordering = ('projeto__nome', 'nome')
    # Permite buscar o Projeto pai por campo de busca (Raw ID Field)
    raw_id_fields = ('projeto',)


# O modelo Registro será criado em seguida, em uma etapa separada para focar
# na complexidade das relações M2M e FK.
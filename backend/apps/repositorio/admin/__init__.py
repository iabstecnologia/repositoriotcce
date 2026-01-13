from django.contrib import admin
from django.utils.safestring import mark_safe
from django.db.models import Q

from ..models import (
    Projeto, Subprojeto, Autor, Tag, TipoDocumento,
    AreaTematica, Status, TipoPublicacao, Registro
)


# ==========================================
# ADMIN PARA MODELOS AUXILIARES/LOOKUP
# ==========================================

@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome',)
    ordering = ('nome',)


@admin.register(AreaTematica)
class AreaTematicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome',)
    ordering = ('nome',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('nome', 'is_public', 'ativo')
    list_filter = ('is_public', 'ativo')
    search_fields = ('nome',)
    ordering = ('nome',)


@admin.register(TipoPublicacao)
class TipoPublicacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome',)
    ordering = ('nome',)


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'lattes_id', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome', 'lattes_id')
    ordering = ('nome',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome',)
    ordering = ('nome',)


# ==========================================
# ADMIN PARA ESTRUTURA HIERÁRQUICA
# ==========================================

class SubprojetoInline(admin.TabularInline):
    """Inline para gerenciar Subprojetos dentro do Projeto."""
    model = Subprojeto
    extra = 1
    fields = ('nome', 'ativo')
    ordering = ('nome',)


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'contador_subprojetos')
    list_filter = ('ativo',)
    search_fields = ('nome',)
    ordering = ('nome',)
    inlines = [SubprojetoInline]

    def contador_subprojetos(self, obj):
        """Retorna o número de subprojetos."""
        return obj.subprojetos.count()
    contador_subprojetos.short_description = 'Subprojetos'


@admin.register(Subprojeto)
class SubprojetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'projeto', 'ativo')
    list_filter = ('projeto', 'ativo')
    search_fields = ('nome', 'projeto__nome')
    ordering = ('projeto', 'nome')


# ==========================================
# INLINES PARA REGISTRO (M2M)
# ==========================================

class AutorInline(admin.TabularInline):
    """Inline para gerenciar M2M Autores."""
    model = Registro.autores.through
    extra = 1
    verbose_name = "Autor"
    verbose_name_plural = "Autores"


class TagInline(admin.TabularInline):
    """Inline para gerenciar M2M Tags."""
    model = Registro.tags.through
    extra = 1
    verbose_name = "Tag"
    verbose_name_plural = "Tags"


# ==========================================
# ADMIN PARA REGISTRO (PRINCIPAL)
# ==========================================

@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    """
    Admin para Registro com auditoria automática (Option A),
    filtros completos (Option B) e inlines para M2M.
    """

    list_display = (
        'titulo_resumido',
        'subprojeto',
        'tipo_publicacao',
        'area_tematica',
        'status',
        'data_publicacao',
        'ativo',
        'usuario_criacao',
        'date_create_short'
    )

    list_filter = (
        'ativo',
        'tipo_documento',
        'area_tematica',
        'tipo_publicacao',
        'status',
        ('data_publicacao', admin.DateFieldListFilter),
        'subprojeto__projeto',
        'subprojeto',
        'usuario_criacao',
        'date_create',
    )

    search_fields = (
        'titulo',
        'resumo',
        'isbn',
        'subprojeto__nome',
        'autores__nome',
        'tags__nome',
    )

    readonly_fields = (
        'date_create',
        'date_update',
        'usuario_criacao',
        'usuario_ultima_atualizacao',
    )

    fieldsets = (
        ('Identificação', {
            'fields': ('titulo', 'resumo', 'data_publicacao'),
        }),
        ('Estrutura e Classificação', {
            'fields': (
                'subprojeto',
                'tipo_documento',
                'area_tematica',
                'tipo_publicacao',
                'status',
            ),
        }),
        ('Conteúdo e Arquivo', {
            'fields': ('arquivo', 'link_externo', 'isbn'),
        }),
        ('Auditoria e Controle', {
            'fields': (
                'ativo',
                'date_create',
                'date_update',
                'usuario_criacao',
                'usuario_ultima_atualizacao',
            ),
            'classes': ('collapse',),
        }),
    )

    inlines = [AutorInline, TagInline]

    ordering = ('-data_publicacao', 'titulo')

    # =============================================
    # OPTION A: Auditoria Automática
    # =============================================

    def save_model(self, request, obj, form, change):
        """
        Sobrescreve save_model para preencher automaticamente
        usuario_criacao e usuario_ultima_atualizacao.
        """
        if not change:  # Criação (não é alteração)
            obj.usuario_criacao = request.user
        obj.usuario_ultima_atualizacao = request.user
        super().save_model(request, obj, form, change)

    # =============================================
    # MÉTODOS DE EXIBIÇÃO
    # =============================================

    def titulo_resumido(self, obj):
        """Exibe título truncado para melhor legibilidade na lista."""
        if len(obj.titulo) > 60:
            return f"{obj.titulo[:60]}..."
        return obj.titulo
    titulo_resumido.short_description = 'Título'

    def date_create_short(self, obj):
        """Exibe data_create em formato curto."""
        return obj.date_create.strftime('%d/%m/%Y %H:%M')
    date_create_short.short_description = 'Criado em'

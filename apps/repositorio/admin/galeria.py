from django.contrib import admin
from django.utils.html import format_html

from ..models.repositorio import FotoGaleria


@admin.register(FotoGaleria)
class FotoGaleriaAdmin(admin.ModelAdmin):
    """Configuracao admin para fotos da galeria."""
    list_display = ('titulo', 'ordem', 'ativo', 'preview_imagem', 'date_update')
    list_filter = ('ativo',)
    search_fields = ('titulo', 'descricao')
    ordering = ('ordem', '-date_update')
    readonly_fields = ('date_create', 'date_update', 'usuario_criacao', 'usuario_ultima_atualizacao')

    fieldsets = (
        ('Informacoes da Imagem', {
            'fields': ('titulo', 'descricao', 'imagem', 'ordem', 'ativo')
        }),
        ('Auditoria', {
            'fields': ('date_create', 'date_update', 'usuario_criacao', 'usuario_ultima_atualizacao'),
            'classes': ('collapse',)
        })
    )

    def preview_imagem(self, obj):
        if obj.imagem and obj.imagem.url:
            return format_html(
                '<img src="{}" style="height: 40px; width: 60px; object-fit: cover;" />',
                obj.imagem.url
            )
        return '-'

    preview_imagem.short_description = 'Preview'

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario_criacao = request.user
        obj.usuario_ultima_atualizacao = request.user
        super().save_model(request, obj, form, change)

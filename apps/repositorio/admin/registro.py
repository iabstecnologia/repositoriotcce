from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.forms import Textarea
from django.db import models
# Importação relativa para acessar os modelos do app repositorio
from ..models.repositorio import Registro
# Importação direta do modelo User customizado, que está na pasta 'models' do app 'accounts'
from apps.accounts.models.user import User


@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    """Configuração Admin para o modelo principal de documentos (Registro)."""

    # -----------------------------------------------------------
    # LISTA E FILTROS
    # -----------------------------------------------------------
    list_display = (
        'titulo', 'subprojeto_link', 'data_publicacao',
        'status', 'usuario_criacao', 'ativo', 'visualizar_arquivo'
    )

    list_filter = (
        'status__is_public', 'ativo', 'data_publicacao',
        'tipo_documento', 'area_tematica', 'status', 'subprojeto__projeto',
    )

    search_fields = (
        'titulo', 'resumo', 'doi', 'isbn',
        'autores__nome', 'tags__nome', 'subprojeto__nome'
    )

    # Otimização de consultas para a lista de registros
    list_select_related = ('subprojeto', 'status', 'usuario_criacao')

    # -----------------------------------------------------------
    # EDIÇÃO E FORMULÁRIO
    # -----------------------------------------------------------

    # Campos que NUNCA devem ser editáveis
    readonly_fields = (
        'date_create',
        'date_update',
        'usuario_criacao',
        'usuario_ultima_atualizacao'  # MANTIDO AQUI para visualização na Auditoria
    )

    # Define o layout da tela de edição (fieldsets)
    fieldsets = (
        ('Informações Principais', {
            'fields': ('titulo', 'resumo', 'data_publicacao', 'status', 'ativo'),
            'description': 'Informações básicas e controle de publicação.'
        }),
        ('Classificação e Relações', {
            'fields': (
                'subprojeto', 'tipo_documento', 'area_tematica', 'tipo_publicacao',
                'autores', 'tags'
            ),
            'classes': ('wide',),
        }),
        ('Identificadores e Fonte', {
            # O Django deve conseguir encontrar 'doi' e 'isbn' se o modelo for carregado corretamente.
            # Se o erro persistir, o problema está fora deste arquivo.
            'fields': ('isbn', 'arquivo', 'link_externo'),
            'description': 'Identificadores globais (DOI/ISBN) e fonte principal do documento (Arquivo S3 ou Link Externo).'
        }),
        ('Auditoria', {
            # Estes campos estão em readonly_fields, mas precisam ser listados aqui para aparecerem na seção
            'fields': ('date_create', 'date_update', 'usuario_criacao', 'usuario_ultima_atualizacao'),
            'classes': ('collapse',),
        }),
    )

    # Usa Raw ID Field para FKs/M2M que têm muitos registros (Raw ID só para campos não readonly)
    raw_id_fields = (
        'subprojeto',
        # Removido 'usuario_ultima_atualizacao' e 'usuario_criacao' pois são preenchidos automaticamente/readonly
        'autores', 'tags'
    )

    # Sobrescreve o widget de Textarea para campos grandes
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 80})},
    }

    # -----------------------------------------------------------
    # MÉTODOS CUSTOMIZADOS
    # -----------------------------------------------------------
    # (Métodos subprojeto_link e visualizar_arquivo permanecem inalterados)

    def subprojeto_link(self, obj):
        """Cria um link para a edição do subprojeto no admin."""
        link = reverse("admin:repositorio_subprojeto_change", args=[obj.subprojeto.id])
        return format_html('<a href="{}">{}</a>', link, obj.subprojeto)

    subprojeto_link.short_description = 'Subprojeto'

    def visualizar_arquivo(self, obj):
        """Cria um link direto para o arquivo (S3) ou link externo."""
        if obj.arquivo and obj.arquivo.url:
            return format_html('<a href="{}" target="_blank">Download (S3)</a>', obj.arquivo.url)
        if obj.link_externo:
            return format_html('<a href="{}" target="_blank">Link Externo</a>', obj.link_externo)
        return "-"

    visualizar_arquivo.short_description = 'Arquivo/Link'

    # -----------------------------------------------------------
    # CONTROLE DE PERMISSÕES E PREENCHIMENTO AUTOMÁTICO
    # -----------------------------------------------------------

    # Garante que os campos de auditoria sejam preenchidos automaticamente
    def save_model(self, request, obj, form, change):
        if not change:  # Se for a primeira criação
            obj.usuario_criacao = request.user
        obj.usuario_ultima_atualizacao = request.user
        super().save_model(request, obj, form, change)
from django import forms
from apps.repositorio.models import Subprojeto, Autor, Tag, TipoDocumento, AreaTematica, Status, TipoPublicacao
from datetime import datetime


class RepositorioFilterForm(forms.Form):
    """
    Formulário usado para renderizar os filtros avançados no template.
    Não é usado para validação, mas sim para preencher as opções de dropdown.
    """

    # Filtro de Busca Full-Text (Título, Resumo, etc.)
    q = forms.CharField(
        required=False,
        label="Busca por Palavra-chave",
        widget=forms.TextInput(attrs={'placeholder': 'Buscar no repositório...'})
    )

    # Filtros de Seleção (Chaves Estrangeiras e M2M)
    subprojeto = forms.ModelChoiceField(
        queryset=Subprojeto.objects.all(),
        required=False,
        empty_label="Subprojeto (Todos)",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    autor = forms.ModelChoiceField(
        queryset=Autor.objects.all(),
        required=False,
        empty_label="Autor (Todos)",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    tag = forms.ModelChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        empty_label="Tag (Todas)",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    tipo_documento = forms.ModelChoiceField(
        queryset=TipoDocumento.objects.all(),
        required=False,
        empty_label="Tipo de Documento (Todos)",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    area_tematica = forms.ModelChoiceField(
        queryset=AreaTematica.objects.all(),
        required=False,
        empty_label="Área Temática (Todas)",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    status = forms.ModelChoiceField(
        # Lista apenas status públicos para o usuário final
        queryset=Status.objects.filter(is_public=True),
        required=False,
        empty_label="Status (Todos)",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    tipo_publicacao = forms.ModelChoiceField(
        queryset=TipoPublicacao.objects.all(),
        required=False,
        empty_label="Veículo de Publicação (Todos)",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    # Filtro por Ano de Publicação (Usaremos apenas o ano)
    ano = forms.IntegerField(
        required=False,
        label="Ano de Publicação",
        min_value=1900,
        max_value=datetime.now().year,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ano'})
    )

    # Filtro de Ordenação (não precisa de ModelForm)
    ordenar_por = forms.ChoiceField(
        required=False,
        choices=[
            ('-data_publicacao', 'Mais Recente'),
            ('data_publicacao', 'Mais Antigo'),
            ('titulo', 'Título (A-Z)'),
        ],
        initial='-data_publicacao',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

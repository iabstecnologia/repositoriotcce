from django import forms
from datetime import datetime

from apps.repositorio.models import (
    Projeto,
    Subprojeto,
    Autor,
    TipoDocumento,
    AreaTematica,
    Status,
    SubAreaTematica,
)
from apps.core.utils.filtros_publicos import (
    projetos_em_uso,
    subprojetos_em_uso,
    autores_em_uso,
    tipos_documento_em_uso,
    areas_tematicas_em_uso,
    subareas_tematicas_em_uso,
    status_em_uso,
)


class RepositorioFilterForm(forms.Form):
    """
    Formulário usado para renderizar os filtros avançados no template.
    Não é usado para validação, mas sim para preencher as opções de dropdown.
    Os querysets são preenchidos no __init__ usando os helpers de filtros_publicos,
    que retornam apenas metadados EM USO (com pelo menos um registro público vinculado).
    """

    # Filtro de Busca Full-Text (Título, Resumo, etc.)
    q = forms.CharField(
        required=False,
        label="Busca por Palavra-chave",
        widget=forms.TextInput(attrs={'placeholder': 'Buscar no repositório...'})
    )

    # Filtros de Seleção (Chaves Estrangeiras e M2M)
    projeto = forms.ModelChoiceField(
        queryset=Projeto.objects.none(),
        required=False,
        empty_label="Projeto (Todos)",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    subprojeto = forms.ModelChoiceField(
        queryset=Subprojeto.objects.none(),
        required=False,
        empty_label="Subprojeto (Todos)",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    autor = forms.ModelChoiceField(
        queryset=Autor.objects.none(),
        required=False,
        empty_label="Autor (Todos)",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    tipo_documento = forms.ModelChoiceField(
        queryset=TipoDocumento.objects.none(),
        required=False,
        empty_label="Tipo de Documento (Todos)",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    area_tematica = forms.ModelChoiceField(
        queryset=AreaTematica.objects.none(),
        required=False,
        empty_label="Área Temática (Todas)",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    subarea_tematica = forms.ModelChoiceField(
        queryset=SubAreaTematica.objects.none(),
        required=False,
        empty_label="Subárea Temática (Todas)",
        label="Subárea Temática",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    status = forms.ModelChoiceField(
        queryset=Status.objects.none(),
        required=False,
        empty_label="Status (Todos)",
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ─────────────────────────────────────────────────────────────
        # Preenche os querysets com apenas metadados EM USO (público)
        # ─────────────────────────────────────────────────────────────
        self.fields['projeto'].queryset = projetos_em_uso()
        self.fields['autor'].queryset = autores_em_uso()
        self.fields['tipo_documento'].queryset = tipos_documento_em_uso()
        self.fields['area_tematica'].queryset = areas_tematicas_em_uso()
        self.fields['subarea_tematica'].queryset = subareas_tematicas_em_uso()
        self.fields['status'].queryset = status_em_uso()

        # Subprojeto em cascata: se há um projeto selecionado (via GET),
        # filtra os subprojetos daquele projeto. Caso contrário, todos em uso.
        projeto_id = None
        if self.is_bound:
            projeto_id = self.data.get('projeto')
        elif self.initial:
            projeto_id = self.initial.get('projeto')

        if projeto_id:
            self.fields['subprojeto'].queryset = subprojetos_em_uso(projeto_id)
        else:
            self.fields['subprojeto'].queryset = subprojetos_em_uso()
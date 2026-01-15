from django import forms
from django.core.exceptions import ValidationError
from apps.repositorio.models.repositorio import (
    Registro, Subprojeto, Autor, Tag, TipoDocumento,
    AreaTematica, Status, TipoPublicacao
)


class RegistroForm(forms.ModelForm):
    """Formulário para criação e edição de Registros."""
    
    class Meta:
        model = Registro
        fields = [
            'titulo', 'resumo', 'subprojeto', 'autores', 'tags',
            'tipo_documento', 'area_tematica', 'status', 'tipo_publicacao',
            'data_publicacao', 'isbn', 'arquivo', 'link_externo', 'ativo'
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o título do documento'
            }),
            'resumo': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Descreva o conteúdo do documento'
            }),
            'subprojeto': forms.Select(attrs={'class': 'form-select'}),
            'autores': forms.CheckboxSelectMultiple(),
            'tags': forms.CheckboxSelectMultiple(),
            'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
            'area_tematica': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'tipo_publicacao': forms.Select(attrs={'class': 'form-select'}),
            'data_publicacao': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 978-3-16-148410-0'
            }),
            'arquivo': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'link_externo': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://exemplo.com/documento'
            }),
            'ativo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
        labels = {
            'titulo': 'Título do Documento',
            'resumo': 'Resumo/Abstract',
            'subprojeto': 'Subprojeto',
            'autores': 'Autores',
            'tags': 'Palavras-chave',
            'tipo_documento': 'Tipo de Documento',
            'area_tematica': 'Área Temática',
            'status': 'Status',
            'tipo_publicacao': 'Tipo de Publicação',
            'data_publicacao': 'Data de Publicação',
            'isbn': 'ISBN',
            'arquivo': 'Arquivo (PDF, Imagem, etc.)',
            'link_externo': 'Link Externo',
            'ativo': 'Ativo'
        }
        help_texts = {
            'arquivo': 'Faça upload do arquivo ou forneça um link externo.',
            'link_externo': 'Informe a URL se o documento estiver hospedado externamente.',
            'isbn': 'Apenas se aplicável.'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtra apenas registros ativos para os selects
        self.fields['subprojeto'].queryset = Subprojeto.objects.filter(ativo=True)
        self.fields['autores'].queryset = Autor.objects.filter(ativo=True)
        self.fields['tags'].queryset = Tag.objects.filter(ativo=True)
        self.fields['tipo_documento'].queryset = TipoDocumento.objects.filter(ativo=True)
        self.fields['area_tematica'].queryset = AreaTematica.objects.filter(ativo=True)
        self.fields['status'].queryset = Status.objects.filter(ativo=True)
        self.fields['tipo_publicacao'].queryset = TipoPublicacao.objects.filter(ativo=True)

    def clean(self):
        """Validação adicional do formulário."""
        cleaned_data = super().clean()
        arquivo = cleaned_data.get('arquivo')
        link_externo = cleaned_data.get('link_externo')

        # Validação: deve ter arquivo OU link externo
        if not arquivo and not link_externo:
            raise ValidationError(
                'Você deve fornecer um arquivo para upload OU um link externo.'
            )

        return cleaned_data

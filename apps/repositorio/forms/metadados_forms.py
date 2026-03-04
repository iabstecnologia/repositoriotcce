from django import forms

from apps.repositorio.models.repositorio import (
    Subprojeto,
    TipoDocumento,
    AreaTematica,
    TipoPublicacao,
    Autor,
    Tag,
    Projeto,
)


class SubprojetoForm(forms.ModelForm):
    class Meta:
        model = Subprojeto
        fields = ['projeto', 'nome', 'ativo']
        widgets = {
            'projeto': forms.Select(attrs={'class': 'form-select'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do subprojeto'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'projeto': 'Projeto',
            'nome': 'Subprojeto',
            'ativo': 'Ativo',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['projeto'].queryset = Projeto.objects.filter(ativo=True)


class TipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = TipoDocumento
        fields = ['nome', 'ativo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo de documento'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'nome': 'Tipo de Documento',
            'ativo': 'Ativo',
        }


class AreaTematicaForm(forms.ModelForm):
    class Meta:
        model = AreaTematica
        fields = ['nome', 'ativo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Área temática'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'nome': 'Área Temática',
            'ativo': 'Ativo',
        }


class TipoPublicacaoForm(forms.ModelForm):
    class Meta:
        model = TipoPublicacao
        fields = ['nome', 'ativo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo de publicação'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'nome': 'Tipo de Publicação',
            'ativo': 'Ativo',
        }


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'lattes_id', 'ativo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo do autor'}),
            'lattes_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ID Lattes (opcional)'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'nome': 'Autor',
            'lattes_id': 'ID Lattes',
            'ativo': 'Ativo',
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['nome', 'ativo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Palavra-chave'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'nome': 'Palavra-chave',
            'ativo': 'Ativo',
        }

from django import forms
from apps.repositorio.models.repositorio import FotoGaleria


class FotoGaleriaForm(forms.ModelForm):
    """Formulario para criacao e edicao de fotos da galeria."""

    class Meta:
        model = FotoGaleria
        fields = ['titulo', 'descricao', 'imagem', 'ordem', 'ativo']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o titulo da imagem'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descricao curta da imagem (opcional)'
            }),
            'imagem': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'ordem': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0
            }),
            'ativo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
        labels = {
            'titulo': 'Titulo',
            'descricao': 'Descricao',
            'imagem': 'Imagem',
            'ordem': 'Ordem de exibicao',
            'ativo': 'Ativo'
        }

    def save(self, commit=True):
        """Remove imagem anterior do storage quando o usuario substituir o arquivo."""
        imagem_anterior = None

        if self.instance.pk:
            imagem_anterior = FotoGaleria.objects.filter(pk=self.instance.pk).values_list('imagem', flat=True).first()

        instance = super().save(commit=commit)

        if imagem_anterior:
            nova_imagem = instance.imagem.name if instance.imagem else ''
            if imagem_anterior != nova_imagem:
                storage = instance._meta.get_field('imagem').storage
                if storage.exists(imagem_anterior):
                    storage.delete(imagem_anterior)

        return instance

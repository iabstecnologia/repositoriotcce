from django import forms
from django.core.exceptions import ValidationError
from django.db import transaction
from apps.repositorio.models.repositorio import (
    Registro, Projeto, Subprojeto, Autor, Tag, TipoDocumento,
    AreaTematica, Status, TipoPublicacao
)


class RegistroForm(forms.ModelForm):
    """Formulário para criação e edição de Registros."""
    data_publicacao = forms.DateField(
        required=False,
        input_formats=['%Y-%m-%d', '%d/%m/%Y'],
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'class': 'form-control',
                'type': 'date'
            }
        )
    )

    novo_projeto_subprojeto = forms.ModelChoiceField(
        queryset=Projeto.objects.none(),
        required=False,
        empty_label='Selecione o projeto',
        label='Projeto do novo Subprojeto',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    novo_subprojeto = forms.CharField(
        required=False,
        label='Novo Subprojeto',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Cadastrar novo subprojeto'
            }
        )
    )

    novo_tipo_documento = forms.CharField(
        required=False,
        label='Novo Tipo de Documento',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Cadastrar novo tipo de documento'
            }
        )
    )

    nova_area_tematica = forms.CharField(
        required=False,
        label='Nova Área Temática',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Cadastrar nova área temática'
            }
        )
    )

    novo_tipo_publicacao = forms.CharField(
        required=False,
        label='Novo Tipo de Publicação',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Cadastrar novo tipo de publicação'
            }
        )
    )

    novos_autores = forms.CharField(required=False, widget=forms.HiddenInput())
    novas_tags = forms.CharField(required=False, widget=forms.HiddenInput())
    
    class Meta:
        model = Registro
        fields = [
            'titulo', 'subprojeto', 'autores', 'tags',
            'tipo_documento', 'area_tematica', 'status', 'tipo_publicacao',
            'data_publicacao', 'isbn', 'arquivo', 'link_externo', 'ativo'
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o título do documento'
            }),
            'subprojeto': forms.Select(attrs={'class': 'form-select'}),
            'autores': forms.SelectMultiple(attrs={'class': 'form-select', 'size': 8}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-select', 'size': 8}),
            'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
            'area_tematica': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'tipo_publicacao': forms.Select(attrs={'class': 'form-select'}),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 978-3-16-148410-0'
            }),
            'arquivo': forms.ClearableFileInput(attrs={
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
        self.fields['novo_projeto_subprojeto'].queryset = Projeto.objects.filter(ativo=True)
        self.fields['subprojeto'].queryset = Subprojeto.objects.filter(ativo=True)
        self.fields['autores'].queryset = Autor.objects.filter(ativo=True)
        self.fields['tags'].queryset = Tag.objects.filter(ativo=True)
        self.fields['tipo_documento'].queryset = TipoDocumento.objects.filter(ativo=True)
        self.fields['area_tematica'].queryset = AreaTematica.objects.filter(ativo=True)
        self.fields['status'].queryset = Status.objects.filter(ativo=True)
        self.fields['tipo_publicacao'].queryset = TipoPublicacao.objects.filter(ativo=True)

        self.fields['subprojeto'].required = False
        self.fields['tipo_documento'].required = False
        self.fields['area_tematica'].required = False
        self.fields['tipo_publicacao'].required = False
        self.fields['autores'].required = False
        self.fields['tags'].required = False

    @staticmethod
    def _normalize_text(value):
        if not value:
            return ''
        return ' '.join(value.strip().split())

    def _parse_hidden_items(self, key):
        raw = self.cleaned_data.get(key) or ''
        normalized = []
        for item in raw.split('|'):
            item_normalized = self._normalize_text(item)
            if item_normalized and item_normalized not in normalized:
                normalized.append(item_normalized)
        return normalized

    def _resolve_tipo_documento(self):
        tipo_documento = self.cleaned_data.get('tipo_documento')
        novo_tipo_documento = self._normalize_text(self.cleaned_data.get('novo_tipo_documento'))

        if tipo_documento:
            return tipo_documento

        if novo_tipo_documento:
            existente = TipoDocumento.objects.filter(nome__iexact=novo_tipo_documento).first()
            if existente:
                return existente
            return TipoDocumento.objects.create(nome=novo_tipo_documento, ativo=True)

        return None

    def _resolve_area_tematica(self):
        area_tematica = self.cleaned_data.get('area_tematica')
        nova_area_tematica = self._normalize_text(self.cleaned_data.get('nova_area_tematica'))

        if area_tematica:
            return area_tematica

        if nova_area_tematica:
            existente = AreaTematica.objects.filter(nome__iexact=nova_area_tematica).first()
            if existente:
                return existente
            return AreaTematica.objects.create(nome=nova_area_tematica, ativo=True)

        return None

    def _resolve_tipo_publicacao(self):
        tipo_publicacao = self.cleaned_data.get('tipo_publicacao')
        novo_tipo_publicacao = self._normalize_text(self.cleaned_data.get('novo_tipo_publicacao'))

        if tipo_publicacao:
            return tipo_publicacao

        if novo_tipo_publicacao:
            existente = TipoPublicacao.objects.filter(nome__iexact=novo_tipo_publicacao).first()
            if existente:
                return existente
            return TipoPublicacao.objects.create(nome=novo_tipo_publicacao, ativo=True)

        return None

    def _resolve_subprojeto(self):
        subprojeto = self.cleaned_data.get('subprojeto')
        novo_subprojeto = self._normalize_text(self.cleaned_data.get('novo_subprojeto'))
        novo_projeto_subprojeto = self.cleaned_data.get('novo_projeto_subprojeto')

        if subprojeto:
            return subprojeto

        if novo_subprojeto and novo_projeto_subprojeto:
            existente = Subprojeto.objects.filter(
                projeto=novo_projeto_subprojeto,
                nome__iexact=novo_subprojeto
            ).first()
            if existente:
                return existente
            return Subprojeto.objects.create(
                projeto=novo_projeto_subprojeto,
                nome=novo_subprojeto,
                ativo=True
            )

        return None

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

        if not cleaned_data.get('subprojeto') and not self._normalize_text(cleaned_data.get('novo_subprojeto')):
            self.add_error('subprojeto', 'Selecione um subprojeto existente ou informe um novo subprojeto.')

        if self._normalize_text(cleaned_data.get('novo_subprojeto')) and not cleaned_data.get('novo_projeto_subprojeto'):
            self.add_error('novo_projeto_subprojeto', 'Selecione o projeto para cadastrar o novo subprojeto.')

        if not cleaned_data.get('tipo_documento') and not self._normalize_text(cleaned_data.get('novo_tipo_documento')):
            self.add_error('tipo_documento', 'Selecione um tipo de documento ou cadastre um novo.')

        if not cleaned_data.get('area_tematica') and not self._normalize_text(cleaned_data.get('nova_area_tematica')):
            self.add_error('area_tematica', 'Selecione uma área temática ou cadastre uma nova.')

        if not cleaned_data.get('tipo_publicacao') and not self._normalize_text(cleaned_data.get('novo_tipo_publicacao')):
            self.add_error('tipo_publicacao', 'Selecione um tipo de publicação ou cadastre um novo.')

        autores_existentes = cleaned_data.get('autores')
        novos_autores = self._parse_hidden_items('novos_autores')
        if not autores_existentes and not novos_autores:
            self.add_error('autores', 'Selecione pelo menos um autor ou cadastre um novo.')

        tags_existentes = cleaned_data.get('tags')
        novas_tags = self._parse_hidden_items('novas_tags')
        if not tags_existentes and not novas_tags:
            self.add_error('tags', 'Selecione pelo menos uma palavra-chave ou cadastre uma nova.')

        return cleaned_data

    def save(self, commit=True):
        """Remove arquivo antigo do storage quando o usuário limpar ou substituir o anexo."""
        arquivo_anterior = None

        if self.instance.pk:
            arquivo_anterior = Registro.objects.filter(pk=self.instance.pk).values_list('arquivo', flat=True).first()

        with transaction.atomic():
            instance = super().save(commit=False)
            instance.subprojeto = self._resolve_subprojeto()
            instance.tipo_documento = self._resolve_tipo_documento()
            instance.area_tematica = self._resolve_area_tematica()
            instance.tipo_publicacao = self._resolve_tipo_publicacao()

            if commit:
                instance.save()
                self.save_m2m()

                autores_ids = [autor.id for autor in self.cleaned_data.get('autores', [])]
                for nome_autor in self._parse_hidden_items('novos_autores'):
                    autor = Autor.objects.filter(nome__iexact=nome_autor).first()
                    if not autor:
                        autor = Autor.objects.create(nome=nome_autor, ativo=True)
                    if autor.id not in autores_ids:
                        autores_ids.append(autor.id)

                if autores_ids:
                    instance.autores.set(autores_ids)

                tags_ids = [tag.id for tag in self.cleaned_data.get('tags', [])]
                for nome_tag in self._parse_hidden_items('novas_tags'):
                    tag = Tag.objects.filter(nome__iexact=nome_tag).first()
                    if not tag:
                        tag = Tag.objects.create(nome=nome_tag, ativo=True)
                    if tag.id not in tags_ids:
                        tags_ids.append(tag.id)

                if tags_ids:
                    instance.tags.set(tags_ids)

        if arquivo_anterior:
            novo_arquivo = instance.arquivo.name if instance.arquivo else ''
            if arquivo_anterior != novo_arquivo:
                storage = instance._meta.get_field('arquivo').storage
                if storage.exists(arquivo_anterior):
                    storage.delete(arquivo_anterior)

        return instance

from django import forms
from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models.functions import Lower
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
            'link_externo': 'Link Externo / URL do Vídeo',
            'ativo': 'Ativo'
        }
        help_texts = {
            'arquivo': 'Faça upload do arquivo. Nota: Vídeos devem usar apenas links.',
            'link_externo': 'Informe a URL se o documento estiver hospedado externamente. Para vídeos, este campo é obrigatório.',
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
        self.fields['tipo_documento'].required = True
        self.fields['area_tematica'].required = True
        self.fields['tipo_publicacao'].required = True
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

    def _resolve_subprojeto(self):
        subprojeto = self.cleaned_data.get('subprojeto')
        novo_subprojeto = self._normalize_text(self.cleaned_data.get('novo_subprojeto'))
        novo_projeto_subprojeto = self.cleaned_data.get('novo_projeto_subprojeto')

        if subprojeto:
            return subprojeto

        if novo_subprojeto and novo_projeto_subprojeto:
            existente = Subprojeto.objects.annotate(
                nome_normalizado=Lower('nome')
            ).filter(
                projeto=novo_projeto_subprojeto,
                nome_normalizado=novo_subprojeto.lower()
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
        tipo_documento = cleaned_data.get('tipo_documento')
        novo_subprojeto = self._normalize_text(cleaned_data.get('novo_subprojeto'))

        # Verifica se é um vídeo
        is_video = tipo_documento and 'vídeo' in tipo_documento.nome.lower()

        # Validação: vídeos requerem APENAS link, outros tipos precisam de arquivo OU link
        if is_video:
            if arquivo:
                self.add_error('arquivo', 'Vídeos devem ser cadastrados apenas com links, não com arquivos de upload.')
            if not link_externo:
                self.add_error('link_externo', 'Vídeos requerem um link externo.')
        else:
            if not arquivo and not link_externo:
                raise ValidationError(
                    'Você deve fornecer um arquivo para upload OU um link externo.'
                )

        if not cleaned_data.get('subprojeto') and not novo_subprojeto:
            self.add_error('subprojeto', 'Selecione um subprojeto existente ou informe um novo subprojeto.')

        if novo_subprojeto and not cleaned_data.get('novo_projeto_subprojeto'):
            self.add_error('novo_projeto_subprojeto', 'Selecione o projeto para cadastrar o novo subprojeto.')

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
        """Remove arquivo antigo do storage e processa autores/tags dinâmicos."""
        arquivo_anterior = None

        if self.instance.pk:
            arquivo_anterior = Registro.objects.filter(pk=self.instance.pk).values_list('arquivo', flat=True).first()

        with transaction.atomic():
            instance = super().save(commit=False)
            instance.subprojeto = self._resolve_subprojeto()

            if commit:
                instance.save()

                # --- CORREÇÃO: Inicializa a lista de IDs de autores vindos do formulário ---
                autores_ids = [autor.id for autor in self.cleaned_data.get('autores', [])]

                # Processamento de Novos Autores
                novos_autores = self._parse_hidden_items('novos_autores')
                if novos_autores:
                    autores_existentes = Autor.objects.filter(nome__in=novos_autores)
                    autores_por_nome = {autor.nome: autor for autor in autores_existentes}

                    for nome_autor in novos_autores:
                        autor = autores_por_nome.get(nome_autor)
                        if not autor:
                            autor = Autor.objects.create(nome=nome_autor, ativo=True)
                            autores_por_nome[nome_autor] = autor
                        
                        if autor.id not in autores_ids:
                            autores_ids.append(autor.id)

                if autores_ids:
                    instance.autores.set(autores_ids)

                # Processamento de Tags (Versão otimizada com Lower case)
                tags_ids = [tag.id for tag in self.cleaned_data.get('tags', [])]
                novas_tags = self._parse_hidden_items('novas_tags')
                
                if novas_tags:
                    tags_existentes = {
                        tag.nome_normalizado: tag
                        for tag in Tag.objects.annotate(nome_normalizado=Lower('nome')).filter(
                            nome_normalizado__in=[nome.lower() for nome in novas_tags]
                        )
                    }

                    for nome_tag in novas_tags:
                        chave_tag = nome_tag.lower()
                        tag = tags_existentes.get(chave_tag)
                        if not tag:
                            tag = Tag.objects.create(nome=nome_tag, ativo=True)
                            tags_existentes[chave_tag] = tag
                        
                        if tag.id not in tags_ids:
                            tags_ids.append(tag.id)

                if tags_ids:
                    instance.tags.set(tags_ids)

        # Lógica de limpeza de arquivo físico
        if arquivo_anterior:
            novo_arquivo = instance.arquivo.name if instance.arquivo else ''
            if arquivo_anterior != novo_arquivo:
                storage = instance._meta.get_field('arquivo').storage
                if storage.exists(arquivo_anterior):
                    storage.delete(arquivo_anterior)

        return instance

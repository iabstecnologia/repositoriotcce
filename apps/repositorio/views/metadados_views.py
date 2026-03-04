from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from apps.repositorio.forms.metadados_forms import (
    AreaTematicaForm,
    AutorForm,
    SubprojetoForm,
    TagForm,
    TipoDocumentoForm,
    TipoPublicacaoForm,
)
from apps.repositorio.models.repositorio import (
    AreaTematica,
    Autor,
    Projeto,
    Subprojeto,
    Tag,
    TipoDocumento,
    TipoPublicacao,
)


class BaseMetadataListView(LoginRequiredMixin, ListView):
    login_url = '/admin/login/'
    paginate_by = 20
    search_fields = ['nome']
    context_object_name = 'itens'

    def get_queryset(self):
        queryset = self.model.objects.all()

        search = self.request.GET.get('q')
        if search:
            query = Q()
            for field in self.search_fields:
                query |= Q(**{f'{field}__icontains': search})
            queryset = queryset.filter(query)

        ativo = self.request.GET.get('ativo')
        if ativo == '1':
            queryset = queryset.filter(ativo=True)
        elif ativo == '0':
            queryset = queryset.filter(ativo=False)

        return queryset.order_by('nome')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        query_params = self.request.GET.copy()
        query_params.pop('page', None)
        context['query_params'] = query_params.urlencode()
        return context


class BaseMetadataCreateView(LoginRequiredMixin, CreateView):
    login_url = '/admin/login/'

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)


class BaseMetadataUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/admin/login/'

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)


class BaseMetadataDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/admin/login/'

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class SubprojetoListView(BaseMetadataListView):
    model = Subprojeto
    template_name = 'repositorio/subprojeto_list.html'
    context_object_name = 'subprojetos'
    search_fields = ['nome', 'projeto__nome']

    def get_queryset(self):
        queryset = self.model.objects.select_related('projeto').all()

        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(
                Q(nome__icontains=search) | Q(projeto__nome__icontains=search)
            )

        projeto_id = self.request.GET.get('projeto')
        if projeto_id:
            queryset = queryset.filter(projeto_id=projeto_id)

        ativo = self.request.GET.get('ativo')
        if ativo == '1':
            queryset = queryset.filter(ativo=True)
        elif ativo == '0':
            queryset = queryset.filter(ativo=False)

        return queryset.order_by('projeto__nome', 'nome')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projetos'] = Projeto.objects.filter(ativo=True).order_by('nome')
        return context


class SubprojetoCreateView(BaseMetadataCreateView):
    model = Subprojeto
    form_class = SubprojetoForm
    template_name = 'repositorio/metadado_form.html'
    success_url = reverse_lazy('repositorio:subprojeto_lista')
    success_message = 'Subprojeto criado com sucesso!'
    error_message = 'Erro ao criar subprojeto. Verifique os campos.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_name'] = 'Subprojeto'
        return context


class SubprojetoUpdateView(BaseMetadataUpdateView):
    model = Subprojeto
    form_class = SubprojetoForm
    template_name = 'repositorio/metadado_form.html'
    success_url = reverse_lazy('repositorio:subprojeto_lista')
    success_message = 'Subprojeto atualizado com sucesso!'
    error_message = 'Erro ao atualizar subprojeto. Verifique os campos.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_name'] = 'Subprojeto'
        return context


class SubprojetoDeleteView(BaseMetadataDeleteView):
    model = Subprojeto
    template_name = 'repositorio/metadado_confirm_delete.html'
    success_url = reverse_lazy('repositorio:subprojeto_lista')
    context_object_name = 'item'
    success_message = 'Subprojeto excluído com sucesso!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_name'] = 'Subprojeto'
        context['item_name'] = self.object.nome
        return context


class TipoDocumentoListView(BaseMetadataListView):
    model = TipoDocumento
    template_name = 'repositorio/tipodocumento_list.html'
    context_object_name = 'tipos_documento'


class TipoDocumentoCreateView(BaseMetadataCreateView):
    model = TipoDocumento
    form_class = TipoDocumentoForm
    template_name = 'repositorio/metadado_form.html'
    success_url = reverse_lazy('repositorio:tipodocumento_lista')
    success_message = 'Tipo de documento criado com sucesso!'
    error_message = 'Erro ao criar tipo de documento. Verifique os campos.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_name'] = 'Tipo de Documento'
        return context


class TipoDocumentoUpdateView(BaseMetadataUpdateView):
    model = TipoDocumento
    form_class = TipoDocumentoForm
    template_name = 'repositorio/metadado_form.html'
    success_url = reverse_lazy('repositorio:tipodocumento_lista')
    success_message = 'Tipo de documento atualizado com sucesso!'
    error_message = 'Erro ao atualizar tipo de documento. Verifique os campos.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_name'] = 'Tipo de Documento'
        return context


class TipoDocumentoDeleteView(BaseMetadataDeleteView):
    model = TipoDocumento
    template_name = 'repositorio/metadado_confirm_delete.html'
    success_url = reverse_lazy('repositorio:tipodocumento_lista')
    context_object_name = 'item'
    success_message = 'Tipo de documento excluído com sucesso!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_name'] = 'Tipo de Documento'
        context['item_name'] = self.object.nome
        return context


class AreaTematicaListView(BaseMetadataListView):
    model = AreaTematica
    template_name = 'repositorio/areatematica_list.html'
    context_object_name = 'areas_tematicas'


class AreaTematicaCreateView(BaseMetadataCreateView):
    model = AreaTematica
    form_class = AreaTematicaForm
    template_name = 'repositorio/metadado_form.html'
    success_url = reverse_lazy('repositorio:areatematica_lista')
    success_message = 'Área temática criada com sucesso!'
    error_message = 'Erro ao criar área temática. Verifique os campos.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_name'] = 'Área Temática'
        return context


class AreaTematicaUpdateView(BaseMetadataUpdateView):
    model = AreaTematica
    form_class = AreaTematicaForm
    template_name = 'repositorio/metadado_form.html'
    success_url = reverse_lazy('repositorio:areatematica_lista')
    success_message = 'Área temática atualizada com sucesso!'
    error_message = 'Erro ao atualizar área temática. Verifique os campos.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_name'] = 'Área Temática'
        return context


class AreaTematicaDeleteView(BaseMetadataDeleteView):
    model = AreaTematica
    template_name = 'repositorio/metadado_confirm_delete.html'
    success_url = reverse_lazy('repositorio:areatematica_lista')
    context_object_name = 'item'
    success_message = 'Área temática excluída com sucesso!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_name'] = 'Área Temática'
        context['item_name'] = self.object.nome
        return context


class TipoPublicacaoListView(BaseMetadataListView):
    model = TipoPublicacao
    template_name = 'repositorio/tipopublicacao_list.html'
    context_object_name = 'tipos_publicacao'


class TipoPublicacaoCreateView(BaseMetadataCreateView):
    model = TipoPublicacao
    form_class = TipoPublicacaoForm
    template_name = 'repositorio/metadado_form.html'
    success_url = reverse_lazy('repositorio:tipopublicacao_lista')
    success_message = 'Tipo de publicação criado com sucesso!'
    error_message = 'Erro ao criar tipo de publicação. Verifique os campos.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_name'] = 'Tipo de Publicação'
        return context


class TipoPublicacaoUpdateView(BaseMetadataUpdateView):
    model = TipoPublicacao
    form_class = TipoPublicacaoForm
    template_name = 'repositorio/metadado_form.html'
    success_url = reverse_lazy('repositorio:tipopublicacao_lista')
    success_message = 'Tipo de publicação atualizado com sucesso!'
    error_message = 'Erro ao atualizar tipo de publicação. Verifique os campos.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_name'] = 'Tipo de Publicação'
        return context


class TipoPublicacaoDeleteView(BaseMetadataDeleteView):
    model = TipoPublicacao
    template_name = 'repositorio/metadado_confirm_delete.html'
    success_url = reverse_lazy('repositorio:tipopublicacao_lista')
    context_object_name = 'item'
    success_message = 'Tipo de publicação excluído com sucesso!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_name'] = 'Tipo de Publicação'
        context['item_name'] = self.object.nome
        return context


class AutorListView(BaseMetadataListView):
    model = Autor
    template_name = 'repositorio/autor_list.html'
    context_object_name = 'autores'
    search_fields = ['nome', 'lattes_id']


class AutorCreateView(BaseMetadataCreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'repositorio/metadado_form.html'
    success_url = reverse_lazy('repositorio:autor_lista')
    success_message = 'Autor criado com sucesso!'
    error_message = 'Erro ao criar autor. Verifique os campos.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_name'] = 'Autor'
        return context


class AutorUpdateView(BaseMetadataUpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'repositorio/metadado_form.html'
    success_url = reverse_lazy('repositorio:autor_lista')
    success_message = 'Autor atualizado com sucesso!'
    error_message = 'Erro ao atualizar autor. Verifique os campos.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_name'] = 'Autor'
        return context


class AutorDeleteView(BaseMetadataDeleteView):
    model = Autor
    template_name = 'repositorio/metadado_confirm_delete.html'
    success_url = reverse_lazy('repositorio:autor_lista')
    context_object_name = 'item'
    success_message = 'Autor excluído com sucesso!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_name'] = 'Autor'
        context['item_name'] = self.object.nome
        return context


class TagListView(BaseMetadataListView):
    model = Tag
    template_name = 'repositorio/tag_list.html'
    context_object_name = 'tags'


class TagCreateView(BaseMetadataCreateView):
    model = Tag
    form_class = TagForm
    template_name = 'repositorio/metadado_form.html'
    success_url = reverse_lazy('repositorio:tag_lista')
    success_message = 'Palavra-chave criada com sucesso!'
    error_message = 'Erro ao criar palavra-chave. Verifique os campos.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_name'] = 'Palavra-chave'
        return context


class TagUpdateView(BaseMetadataUpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'repositorio/metadado_form.html'
    success_url = reverse_lazy('repositorio:tag_lista')
    success_message = 'Palavra-chave atualizada com sucesso!'
    error_message = 'Erro ao atualizar palavra-chave. Verifique os campos.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_name'] = 'Palavra-chave'
        return context


class TagDeleteView(BaseMetadataDeleteView):
    model = Tag
    template_name = 'repositorio/metadado_confirm_delete.html'
    success_url = reverse_lazy('repositorio:tag_lista')
    context_object_name = 'item'
    success_message = 'Palavra-chave excluída com sucesso!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_name'] = 'Palavra-chave'
        context['item_name'] = self.object.nome
        return context

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.db.models import Q

from apps.repositorio.models.repositorio import Registro
from apps.repositorio.forms.registro_form import RegistroForm


class RegistroListView(LoginRequiredMixin, ListView):
    """Lista todos os registros com busca e filtros."""
    model = Registro
    template_name = 'repositorio/registro_list.html'
    context_object_name = 'registros'
    paginate_by = 20
    login_url = '/admin/login/'

    def get_queryset(self):
        """Aplica filtros e busca."""
        queryset = Registro.objects.select_related(
            'subprojeto__projeto', 'tipo_documento', 'area_tematica', 'status'
        ).prefetch_related('autores', 'tags')

        # Busca por título ou resumo
        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(
                Q(titulo__icontains=search) | Q(resumo__icontains=search)
            )

        # Filtro por status
        status_id = self.request.GET.get('status')
        if status_id:
            queryset = queryset.filter(status_id=status_id)

        # Filtro por tipo de documento
        tipo_doc_id = self.request.GET.get('tipo_documento')
        if tipo_doc_id:
            queryset = queryset.filter(tipo_documento_id=tipo_doc_id)

        # Filtro por subprojeto
        subprojeto_id = self.request.GET.get('subprojeto')
        if subprojeto_id:
            queryset = queryset.filter(subprojeto_id=subprojeto_id)

        return queryset.order_by('-date_create')

    def get_context_data(self, **kwargs):
        """Adiciona dados extras ao contexto."""
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        
        # Para os filtros nos dropdowns
        from apps.repositorio.models.repositorio import Status, TipoDocumento, Subprojeto
        context['status_list'] = Status.objects.filter(ativo=True)
        context['tipos_documento'] = TipoDocumento.objects.filter(ativo=True)
        context['subprojetos'] = Subprojeto.objects.filter(ativo=True)
        
        return context


class RegistroDetailView(LoginRequiredMixin, DetailView):
    """Visualiza detalhes de um registro."""
    model = Registro
    template_name = 'repositorio/registro_detail.html'
    context_object_name = 'registro'
    login_url = '/admin/login/'

    def get_queryset(self):
        return Registro.objects.select_related(
            'subprojeto__projeto', 'tipo_documento', 'area_tematica',
            'status', 'tipo_publicacao', 'usuario_criacao', 'usuario_ultima_atualizacao'
        ).prefetch_related('autores', 'tags')


class RegistroCreateView(LoginRequiredMixin, CreateView):
    """Cria um novo registro."""
    model = Registro
    form_class = RegistroForm
    template_name = 'repositorio/registro_form.html'
    success_url = reverse_lazy('repositorio:lista')
    login_url = '/admin/login/'

    def form_valid(self, form):
        """Atribui o usuário logado aos campos de auditoria."""
        form.instance.usuario_criacao = self.request.user
        form.instance.usuario_ultima_atualizacao = self.request.user
        messages.success(self.request, 'Registro criado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        """Exibe mensagem de erro."""
        messages.error(self.request, 'Erro ao criar registro. Verifique os campos.')
        return super().form_invalid(form)


class RegistroUpdateView(LoginRequiredMixin, UpdateView):
    """Edita um registro existente."""
    model = Registro
    form_class = RegistroForm
    template_name = 'repositorio/registro_form.html'
    success_url = reverse_lazy('repositorio:lista')
    login_url = '/admin/login/'

    def form_valid(self, form):
        """Atualiza o usuário da última atualização."""
        form.instance.usuario_ultima_atualizacao = self.request.user
        messages.success(self.request, 'Registro atualizado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        """Exibe mensagem de erro."""
        messages.error(self.request, 'Erro ao atualizar registro. Verifique os campos.')
        return super().form_invalid(form)


class RegistroDeleteView(LoginRequiredMixin, DeleteView):
    """Exclui um registro."""
    model = Registro
    template_name = 'repositorio/registro_confirm_delete.html'
    success_url = reverse_lazy('repositorio:lista')
    context_object_name = 'registro'
    login_url = '/admin/login/'

    def delete(self, request, *args, **kwargs):
        """Exibe mensagem de sucesso ao deletar."""
        messages.success(self.request, 'Registro excluído com sucesso!')
        return super().delete(request, *args, **kwargs)

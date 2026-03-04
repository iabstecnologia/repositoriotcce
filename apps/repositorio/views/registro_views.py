from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from apps.repositorio.models.repositorio import Registro, Subprojeto
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

        # Filtro por projeto
        projeto_id = self.request.GET.get('projeto')
        if projeto_id:
            queryset = queryset.filter(subprojeto__projeto_id=projeto_id)

        # Filtro por subprojeto
        subprojeto_id = self.request.GET.get('subprojeto')
        if subprojeto_id:
            queryset = queryset.filter(subprojeto_id=subprojeto_id)

        # Filtro por situação ativa/inativa
        ativo = self.request.GET.get('ativo')
        if ativo == '1':
            queryset = queryset.filter(ativo=True)
        elif ativo == '0':
            queryset = queryset.filter(ativo=False)

        return queryset.order_by('-date_create')

    def get_context_data(self, **kwargs):
        """Adiciona dados extras ao contexto."""
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        
        # Para os filtros nos dropdowns
        from apps.repositorio.models.repositorio import Status, TipoDocumento, Projeto, Subprojeto
        context['status_list'] = Status.objects.filter(ativo=True)
        context['tipos_documento'] = TipoDocumento.objects.filter(ativo=True)
        context['projetos'] = Projeto.objects.filter(ativo=True)

        projeto_id = self.request.GET.get('projeto')
        subprojetos = Subprojeto.objects.filter(ativo=True)
        if projeto_id:
            subprojetos = subprojetos.filter(projeto_id=projeto_id)
        context['subprojetos'] = subprojetos

        query_params = self.request.GET.copy()
        query_params.pop('page', None)
        context['query_params'] = query_params.urlencode()
        
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
        list(messages.get_messages(self.request))
        response = super().form_valid(form)
        messages.success(self.request, 'Registro criado com sucesso!')
        return response

    def form_invalid(self, form):
        """Exibe mensagem de erro."""
        list(messages.get_messages(self.request))
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
        list(messages.get_messages(self.request))
        response = super().form_valid(form)
        messages.success(self.request, 'Registro atualizado com sucesso!')
        return response

    def form_invalid(self, form):
        """Exibe mensagem de erro."""
        list(messages.get_messages(self.request))
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


@login_required(login_url='/admin/login/')
def subprojetos_por_projeto_admin(request):
    projeto_id = request.GET.get('projeto_id')

    subprojetos = Subprojeto.objects.filter(ativo=True)
    if projeto_id:
        subprojetos = subprojetos.filter(projeto_id=projeto_id)

    data = [
        {'id': subprojeto.id, 'nome': subprojeto.nome}
        for subprojeto in subprojetos.order_by('nome')
    ]
    return JsonResponse({'subprojetos': data})

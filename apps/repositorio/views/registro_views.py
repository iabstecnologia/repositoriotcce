from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import JsonResponse, FileResponse, HttpResponse
from django.contrib.auth.decorators import login_required
import zipfile
import io
import os
from django.utils.text import slugify
import logging
from django.shortcuts import redirect

logger = logging.getLogger(__name__)


from apps.repositorio.models.repositorio import Registro, Subprojeto
from apps.repositorio.forms.registro_form import RegistroForm


def _mensagem_campos_invalidos(form, acao):
    campos_com_erro = []

    for field_name in form.errors.keys():
        if field_name == '__all__':
            continue

        field = form.fields.get(field_name)
        label = (field.label if field else field_name) or field_name
        label = str(label).strip()

        if label and label not in campos_com_erro:
            campos_com_erro.append(label)

    if form.non_field_errors() and 'Validações gerais' not in campos_com_erro:
        campos_com_erro.append('Validações gerais')

    if campos_com_erro:
        return f"Erro ao {acao} registro. Corrija os campos: {', '.join(campos_com_erro)}."

    return f'Erro ao {acao} registro. Verifique os campos.'


def _apply_filters_to_queryset(query_params):
    """
    Aplica filtros ao queryset baseado nos parâmetros GET.
    Utilizado tanto pela lista quanto pelo download para garantir consistência.
    """
    queryset = Registro.objects.select_related(
        'subprojeto__projeto', 'tipo_documento', 'area_tematica', 'status'
    ).prefetch_related('autores', 'tags')

    # Busca por título ou resumo
    search = query_params.get('q')
    if search:
        queryset = queryset.filter(
            Q(titulo__icontains=search) | Q(resumo__icontains=search)
        )

    # Filtro por status
    status_id = query_params.get('status')
    if status_id:
        queryset = queryset.filter(status_id=status_id)

    # Filtro por tipo de documento
    tipo_doc_id = query_params.get('tipo_documento')
    if tipo_doc_id:
        queryset = queryset.filter(tipo_documento_id=tipo_doc_id)

    # Filtro por projeto
    projeto_id = query_params.get('projeto')
    if projeto_id:
        queryset = queryset.filter(subprojeto__projeto_id=projeto_id)

    # Filtro por subprojeto
    subprojeto_id = query_params.get('subprojeto')
    if subprojeto_id:
        queryset = queryset.filter(subprojeto_id=subprojeto_id)

    # Filtro por situação ativa/inativa
    ativo = query_params.get('ativo')
    if ativo == '1':
        queryset = queryset.filter(ativo=True)
    elif ativo == '0':
        queryset = queryset.filter(ativo=False)

    return queryset.order_by('-date_create')


from django.contrib import messages
from django.shortcuts import redirect

@login_required(login_url='/admin/login/')
def download_filtered_registros(request):
    """
    Download de todos os arquivos filtrados em formato ZIP.
    Organiza os arquivos em estrutura: projeto_slug/subprojeto_slug/arquivo
    """
    try:
        # Aplica os mesmos filtros da listagem
        queryset = _apply_filters_to_queryset(request.GET)
        
        # Filtra apenas registros que possuem arquivo (arquivo não está vazio)
        queryset = queryset.filter(arquivo__isnull=False).exclude(arquivo='')
        
        if not queryset.exists():
            # Quando não houver arquivos:
            messages.warning(request, 'Nenhum arquivo encontrado com os filtros aplicados.')
            # Redireciona de volta para a página de listagem preservando os filtros
            return redirect(f"{reverse_lazy('repositorio:lista')}?{request.GET.urlencode()}")
        
        # Cria arquivo ZIP em memória
        zip_buffer = io.BytesIO()
        arquivos_adicionados = 0
        
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for registro in queryset:
                if not registro.arquivo:
                    continue
                
                try:
                    arquivo = registro.arquivo
                    projeto_slug = slugify(registro.subprojeto.projeto.nome or 'sem-projeto')
                    subprojeto_slug = slugify(registro.subprojeto.nome or 'sem-subprojeto')
                    arquivo_nome = os.path.basename(arquivo.name)
                    zip_path = f"{projeto_slug}/{subprojeto_slug}/{arquivo_nome}"
                    
                    with arquivo.open('rb') as f:
                        arquivo_conteudo = f.read()
                        zip_file.writestr(zip_path, arquivo_conteudo)
                        arquivos_adicionados += 1
                    
                except Exception as e:
                    logger.error(f"Erro ao adicionar arquivo {getattr(registro.arquivo, 'name', 'unknown')}: {str(e)}")
                    continue
        
        # Se nenhum arquivo foi adicionado com sucesso
        if arquivos_adicionados == 0:
            messages.error(request, 'Nenhum arquivo pôde ser lido com sucesso.')
            return redirect(f"{reverse_lazy('repositorio:lista')}?{request.GET.urlencode()}")
        
        zip_buffer.seek(0)
        
        # Retorna o ZIP como download
        response = FileResponse(
            zip_buffer,
            as_attachment=True,
            filename='registros_filtrados.zip',
            content_type='application/zip'
        )
        
        return response
    
    except Exception as e:
        logger.exception(f"Erro no download filtrado: {e}")
        messages.error(request, f'Erro ao gerar download: {str(e)}')
        return redirect(f"{reverse_lazy('repositorio:lista')}?{request.GET.urlencode()}")

class RegistroListView(LoginRequiredMixin, ListView):
    """Lista todos os registros com busca e filtros."""
    model = Registro
    template_name = 'repositorio/registro_list.html'
    context_object_name = 'registros'
    paginate_by = 20
    login_url = '/admin/login/'

    def get_queryset(self):
        """Aplica filtros e busca usando helper method."""
        return _apply_filters_to_queryset(self.request.GET)

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
        # Limpa mensagens pendentes de forma explícita, se necessário
        storage = messages.get_messages(self.request)
        storage.used = True

        response = super().form_valid(form)
        messages.success(self.request, 'Registro criado com sucesso!')
        return response

    def form_invalid(self, form):
        """Exibe mensagem de erro."""
        messages.error(self.request, _mensagem_campos_invalidos(form, 'criar'))
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
        messages.error(self.request, _mensagem_campos_invalidos(form, 'atualizar'))
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

from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, Http404, HttpResponseRedirect, JsonResponse
import os

from apps.core.repository_filters import (
    build_repositorio_filter_context,
    filter_repository_queryset,
)
from apps.repositorio.models.repositorio import Registro, Subprojeto


class RepositorioView(ListView):
    """
    Lista todos os Registros (Documentos) e gerencia a pesquisa avançada e filtros.
    """
    model = Registro
    template_name = 'website/repo_busca.html'
    context_object_name = 'registros'
    paginate_by = 10

    def get_queryset(self):
        """Retorna o queryset público de registros com filtros aplicados."""
        return filter_repository_queryset(self.request.GET)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(build_repositorio_filter_context(self.request.GET))
        return context


def subprojetos_por_projeto(request):
    projeto_id = request.GET.get('projeto_id')
    subprojetos = Subprojeto.objects.filter(projeto_id=projeto_id)

    data = [
        {'id': subprojeto.id, 'nome': subprojeto.nome}
        for subprojeto in subprojetos.order_by('nome')
    ]
    return JsonResponse({'subprojetos': data})

# Função para Download (Mantida)
def download_registro(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
# Função para Download (Mantida)
def download_registro(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    
    # Lógica de download (verifique o campo do seu modelo)
    if not registro.arquivo:
        raise Http404("Arquivo não encontrado.")

    # Tenta usar o arquivo local primeiro
    try:
        filepath = registro.arquivo.path
        filename = os.path.basename(filepath)

        response = FileResponse(open(filepath, 'rb'), content_type='application/force-download')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
    except (FileNotFoundError, AttributeError, ValueError):
        # Se o arquivo local não existir ou não estiver disponível, redireciona para a URL
        # (útil para S3 ou outros backends de armazenamento remoto)
        if registro.arquivo.url:
            return HttpResponseRedirect(registro.arquivo.url)
        raise Http404("Arquivo físico não encontrado no servidor.")


# Função para Visualizar o arquivo
def view_file(request, pk):
    """
    Abre o arquivo localmente para visualização em uma nova aba.
    """
    registro = get_object_or_404(Registro, pk=pk)
    
    if not registro.arquivo:
        raise Http404("Arquivo não encontrado.")

    # Tenta usar o arquivo local primeiro
    try:
        filepath = registro.arquivo.path
        # Retorna o arquivo para visualização no navegador
        response = FileResponse(open(filepath, 'rb'))
        return response
    except (FileNotFoundError, AttributeError, ValueError):
        # Se o arquivo local não existir ou não estiver disponível, redireciona para a URL
        # (útil para S3 ou outros backends de armazenamento remoto)
        if registro.arquivo.url:
            return HttpResponseRedirect(registro.arquivo.url)
        raise Http404("Arquivo físico não encontrado no servidor.")
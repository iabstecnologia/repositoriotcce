from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.shortcuts import render
from datetime import datetime
from apps.repositorio.models.repositorio import Registro, TipoDocumento
from apps.core.forms import RepositorioFilterForm
from django.shortcuts import get_object_or_404
from django.http import FileResponse, Http404, HttpResponseRedirect
import os


class RepositorioView(ListView):
    """
    Lista todos os Registros (Documentos) e gerencia a pesquisa avançada e filtros.
    """
    model = Registro
    template_name = 'website/repo_busca.html'
    context_object_name = 'registros'
    paginate_by = 10

    def get_queryset(self):
        """
        Retorna o queryset base (apenas documentos ativos e públicos) e aplica os filtros
        recebidos via GET.
        """
        # Filtro base: Apenas registros ativos e com status público
        queryset = Registro.objects.filter(
            ativo=True,
            status__is_public=True
        ).prefetch_related(
            'autores', 'tags', 'subprojeto__projeto'  # Otimiza o carregamento de FKs e M2M
        )

        # Obtém os parâmetros de busca da URL
        query = self.request.GET.get('q')
        subprojeto_id = self.request.GET.get('subprojeto')
        autor_id = self.request.GET.get('autor')
        tag_id = self.request.GET.get('tag')
        tipo_documento_id = self.request.GET.get('tipo_documento')
        categoria = self.request.GET.get('categoria')
        area_tematica_id = self.request.GET.get('area_tematica')
        status_id = self.request.GET.get('status')
        tipo_publicacao_id = self.request.GET.get('tipo_publicacao')
        ano = self.request.GET.get('ano')
        ordenar_por = self.request.GET.get('ordenar_por', '-data_publicacao')

        # --- LÓGICA DE FILTRAGEM ---

        # 1. Filtro Full-Text (Título, Resumo, Tags, etc.)
        if query:
            # Usando Q objects para construir uma cláusula OR (busca em múltiplos campos)
            queryset = queryset.filter(
                Q(titulo__icontains=query) |
                Q(resumo__icontains=query) |
                Q(autores__nome__icontains=query) |
                Q(tags__nome__icontains=query)
            ).distinct()  # Necessário devido à busca M2M (autores, tags)

        # 2. Filtros de Seleção (FKs e M2M)
        if subprojeto_id:
            queryset = queryset.filter(subprojeto__id=subprojeto_id)
        if autor_id:
            queryset = queryset.filter(autores__id=autor_id)
        if tag_id:
            queryset = queryset.filter(tags__id=tag_id)
        # Permite filtrar por tipo_documento usando id (padrão) ou por categoria textual
        if tipo_documento_id:
            # Se for um número (id) usa id, senão tenta por nome (icontains)
            if str(tipo_documento_id).isdigit():
                queryset = queryset.filter(tipo_documento__id=tipo_documento_id)
            else:
                queryset = queryset.filter(tipo_documento__nome__icontains=tipo_documento_id)

        # Filtro por categoria via parâmetro 'categoria' (usado pelos cards)
        if categoria:
            # Normaliza removendo espaço e 's' final simples e acentos comuns, tenta match icontains
            norm = categoria.strip()
            # remove 's' final (plural simples)
            if len(norm) > 1 and (norm.endswith('s') or norm.endswith('S')):
                norm = norm[:-1]
            # substituições simples para acentos comuns (ajuda em comparações básicas)
            norm = norm.replace('í','i').replace('Í','I').replace('é','e').replace('É','E').replace('á','a').replace('Á','A').replace('ó','o').replace('Ó','O').replace('ú','u').replace('Ú','U').replace('ã','a').replace('Ã','A').replace('õ','o').replace('Õ','O')
            # Busca por tipo_documento que contenha o termo normalizado
            queryset = queryset.filter(tipo_documento__nome__icontains=norm)
        if area_tematica_id:
            queryset = queryset.filter(area_tematica__id=area_tematica_id)
        if status_id:
            queryset = queryset.filter(status__id=status_id)
        if tipo_publicacao_id:
            queryset = queryset = queryset.filter(tipo_publicacao__id=tipo_publicacao_id)

        # 3. Filtro por Ano
        if ano:
            try:
                ano = int(ano)
                # Filtra pela data_publicacao__year
                queryset = queryset.filter(data_publicacao__year=ano)
            except ValueError:
                pass  # Ignora se o ano for inválido

        # 4. Ordenação
        if ordenar_por:
            queryset = queryset.order_by(ordenar_por)

        return queryset

    def get_context_data(self, **kwargs):
        """
        Adiciona o formulário de filtro e os dados de contexto ao template.
        """
        context = super().get_context_data(**kwargs)

        # Instancia o formulário de filtro, preenchendo-o com os dados da requisição (GET)
        context['form'] = RepositorioFilterForm(self.request.GET)

        # Se for necessário passar o termo de busca para o campo de busca simples no Header
        context['search_term'] = self.request.GET.get('q', '')

        # Carrega todos os TipoDocumento ativos para os cards de categoria
        tipos_documento = TipoDocumento.objects.filter(ativo=True).order_by('nome')
        context['tipos_documento'] = tipos_documento

        # Mapeia categorias simples (nomes dos cards) para IDs de TipoDocumento
        # Esse mapeamento permite que os cards usem links simples e robustos
        # Busca por correspondência parcial (icontains) para flexibilidade
        category_mapping = {
            'Livros': tipos_documento.filter(nome__icontains='Livro').first(),
            'Artigos': tipos_documento.filter(nome__icontains='Artigo').first(),
            'RelatórioTécnico': tipos_documento.filter(nome__icontains='RELATÓRIO').first(),
            'Vídeos': tipos_documento.filter(nome__icontains='Vídeo').first() or tipos_documento.filter(nome__icontains='Video').first(),
        }
        # Manter apenas os tipos que existem no banco; converter para IDs
        context['category_mapping'] = {k: v.id for k, v in category_mapping.items() if v}

        return context

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
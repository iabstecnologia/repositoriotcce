from django.views.generic import TemplateView
from django.db.models import Count, Q, Prefetch

from apps.repositorio.models.repositorio import FotoGaleria, Projeto, Registro, Autor


class HomeView(TemplateView):
    template_name = 'website/home.html'

    def get_context_data(self, **kwargs):
        """
        Adiciona contexto específico para a pagina (futuramente dados de contadores/métricas).
        """
        context = super().get_context_data(**kwargs)
        return context


class TCCEView(TemplateView):
    template_name = 'website/tcce.html'

    def get_context_data(self, **kwargs):
        """
        Adiciona contexto com estatísticas dinâmicas para cada TCCE.
        Mensagens de tabulação para cada projeto TCCE com métricas calculadas do banco de dados.
        """
        context = super().get_context_data(**kwargs)
        
        # IDs dos projetos: 1=TCCE 1/2018, 3=TCCE 2/2020, 4=TCCE 1/2022
        projeto_ids = [1, 3, 4]
        mapeamento_tabs = {1: 'tcce1', 3: 'tcce2', 4: 'tcce3'}
        
        # Dicionário para armazenar estatísticas de cada TCCE
        tcces = {}
        
        for projeto_id in projeto_ids:
            tab_key = mapeamento_tabs[projeto_id]
            stats = self._calcular_estatisticas_tcce(projeto_id)
            tcces[tab_key] = stats
        
        context['tcce1'] = tcces.get('tcce1', {})
        context['tcce2'] = tcces.get('tcce2', {})
        context['tcce3'] = tcces.get('tcce3', {})
        
        return context
    
    def _calcular_estatisticas_tcce(self, projeto_id):
        """
        Calcula as 6 estatísticas principais para um projeto TCCE específico.
        
        Args:
            projeto_id: ID do projeto
            
        Returns:
            Dict com as seguintes chaves:
            - producoes_academicas: Total de registros ativos
            - producoes_publicadas: Total de registros com status PUBLICADO
            - artigos_cientificos: Total de artigos científicos
            - autores_unicos: Total de autores únicos
            - subprojetos_ativos: Total de subprojetos ativos
            - relatorios_tecnicos: Total de relatórios técnicos
        """
        try:
            projeto = Projeto.objects.get(id=projeto_id, ativo=True)
        except Projeto.DoesNotExist:
            # Retorna zeros se projeto não existe
            return {
                'producoes_academicas': 0,
                'producoes_publicadas': 0,
                'artigos_cientificos': 0,
                'autores_unicos': 0,
                'subprojetos_ativos': 0,
                'relatorios_tecnicos': 0,
            }
        
        # Query base para todos os registros do projeto
        registros_queryset = Registro.objects.filter(
            subprojeto__projeto=projeto,
            ativo=True
        ).select_related(
            'subprojeto',
            'subprojeto__projeto',
            'tipo_documento',
            'status'
        ).prefetch_related('autores', 'tags')
        
        # Total de produções acadêmicas (todos os registros ativos)
        producoes_academicas = registros_queryset.count()
        
        # Produções publicadas (status = PUBLICADO)
        producoes_publicadas = registros_queryset.filter(
            status__nome='PUBLICADO'
        ).count()
        
        # Artigos científicos (tipo_documento contém 'ARTIGO')
        artigos_cientificos = registros_queryset.filter(
            tipo_documento__nome__icontains='ARTIGO'
        ).count()
        
        # Autores únicos
        autores_unicos = Autor.objects.filter(
            autores__subprojeto__projeto=projeto,
            ativo=True
        ).distinct().count()
        
        # Subprojetos ativos
        subprojetos_ativos = projeto.subprojetos.filter(ativo=True).count()
        
        # Relatórios técnicos (tipo_documento contém 'RELATÓRIO')
        relatorios_tecnicos = registros_queryset.filter(
            tipo_documento__nome__icontains='RELATÓRIO'
        ).count()
        
        return {
            'producoes_academicas': producoes_academicas,
            'producoes_publicadas': producoes_publicadas,
            'artigos_cientificos': artigos_cientificos,
            'autores_unicos': autores_unicos,
            'subprojetos_ativos': subprojetos_ativos,
            'relatorios_tecnicos': relatorios_tecnicos,
        }


class ContatoView(TemplateView):
    template_name = 'website/contato.html'

    def get_context_data(self, **kwargs):
        """
        Adiciona contexto específico para a pagina (futuramente dados de contadores/métricas).
        """
        context = super().get_context_data(**kwargs)
        return context


class GaleriaView(TemplateView):
    template_name = 'website/galeria.html'

    def get_context_data(self, **kwargs):
        """
        Adiciona contexto específico para a pagina (futuramente dados de contadores/métricas).
        """
        context = super().get_context_data(**kwargs)
        fotos = FotoGaleria.objects.filter(ativo=True).order_by('ordem', '-date_create')
        context['gallery_items'] = [
            {
                'id': foto.id,
                'src': foto.imagem.url,
                'title': foto.titulo,
                'description': foto.descricao or ''
            }
            for foto in fotos
            if foto.imagem
        ]
        return context

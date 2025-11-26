from django.views.generic import TemplateView


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
        Adiciona contexto específico para a pagina (futuramente dados de contadores/métricas).
        """
        context = super().get_context_data(**kwargs)
        return context


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
        return context

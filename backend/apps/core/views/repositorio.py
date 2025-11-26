from django.views.generic import TemplateView


class RepositorioView(TemplateView):
    template_name = 'website/repositorio.html'

    def get_context_data(self, **kwargs):
        """
        Adiciona contexto específico para a pagina (futuramente dados de contadores/métricas).
        """
        context = super().get_context_data(**kwargs)
        return context

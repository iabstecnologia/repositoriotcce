from django.views.generic import ListView
from apps.repositorio.models import Registro


class RepositorioView(ListView):
    model = Registro
    template_name = 'website/repositorio.html'
    context_object_name = 'submissoes'
    paginate_by = 5

    def get_queryset(self):
        """
        Retorna os primeiros 5 registros ordenados pela data de publicação (mais recentes).
        Filtra apenas registros ativos e com status público.
        """
        return Registro.objects.filter(
            ativo=True,
            status__is_public=True
        ).select_related(
            'subprojeto',
            'tipo_documento',
            'area_tematica',
            'status',
            'tipo_publicacao'
        ).prefetch_related(
            'autores',
            'tags'
        ).order_by('-data_publicacao')

    def get_context_data(self, **kwargs):
        """
        Adiciona contexto específico para a página (metadados e informações adicionais).
        """
        context = super().get_context_data(**kwargs)
        context['total_registros'] = Registro.objects.filter(ativo=True, status__is_public=True).count()
        return context

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q

from apps.repositorio.models.repositorio import FotoGaleria
from apps.repositorio.forms.galeria_form import FotoGaleriaForm


class FotoGaleriaListView(LoginRequiredMixin, ListView):
    """Lista de fotos da galeria com busca simples."""
    model = FotoGaleria
    template_name = 'repositorio/galeria_list.html'
    context_object_name = 'fotos'
    paginate_by = 20
    login_url = '/admin/login/'

    def get_queryset(self):
        queryset = FotoGaleria.objects.all()

        search = self.request.GET.get('q')
        if search:
            queryset = queryset.filter(
                Q(titulo__icontains=search) | Q(descricao__icontains=search)
            )

        return queryset.order_by('ordem', '-date_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


class FotoGaleriaCreateView(LoginRequiredMixin, CreateView):
    """Cria uma nova foto da galeria."""
    model = FotoGaleria
    form_class = FotoGaleriaForm
    template_name = 'repositorio/galeria_form.html'
    success_url = reverse_lazy('repositorio:galeria_lista')
    login_url = '/admin/login/'

    def form_valid(self, form):
        form.instance.usuario_criacao = self.request.user
        form.instance.usuario_ultima_atualizacao = self.request.user
        messages.success(self.request, 'Imagem criada com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao criar imagem. Verifique os campos.')
        return super().form_invalid(form)


class FotoGaleriaUpdateView(LoginRequiredMixin, UpdateView):
    """Edita uma foto da galeria."""
    model = FotoGaleria
    form_class = FotoGaleriaForm
    template_name = 'repositorio/galeria_form.html'
    success_url = reverse_lazy('repositorio:galeria_lista')
    login_url = '/admin/login/'

    def form_valid(self, form):
        form.instance.usuario_ultima_atualizacao = self.request.user
        messages.success(self.request, 'Imagem atualizada com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao atualizar imagem. Verifique os campos.')
        return super().form_invalid(form)


class FotoGaleriaDeleteView(LoginRequiredMixin, DeleteView):
    """Exclui uma foto da galeria."""
    model = FotoGaleria
    template_name = 'repositorio/galeria_confirm_delete.html'
    success_url = reverse_lazy('repositorio:galeria_lista')
    context_object_name = 'foto'
    login_url = '/admin/login/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Imagem excluida com sucesso!')
        return super().delete(request, *args, **kwargs)

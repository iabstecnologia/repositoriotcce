"""
Mixins para preservar o contexto de filtros entre list views e CRUD de metadados.
Padrão idêntico ao implementado em RegistroListView.
"""
from django.urls import reverse_lazy


class FiltroContextMixin:
    """
    Mixin base para preservar filtros entre navegações de CRUD.
    
    Cada view define:
        - filtro_session_key: chave única na sessão (ex: 'filtros_subprojeto')
        - filtro_default_url: URL de retorno padrão (a list view da entidade)
    """
    filtro_session_key = None
    filtro_default_url = None

    def get_filtros_salvos(self):
        if not self.filtro_session_key:
            return ''
        return self.request.session.get(self.filtro_session_key, '')

    def salvar_filtros_na_sessao(self):
        if not self.filtro_session_key:
            return

        query_params = self.request.GET.copy()
        query_params.pop('page', None)

        if query_params:
            self.request.session[self.filtro_session_key] = query_params.urlencode()
        else:
            self.request.session.pop(self.filtro_session_key, None)

    def get_url_com_filtros(self):
        if not self.filtro_default_url:
            return reverse_lazy('repositorio:lista')

        base_url = str(self.filtro_default_url)
        filtros = self.get_filtros_salvos()
        return f'{base_url}?{filtros}' if filtros else base_url

    def get_success_url(self):
        return self.get_url_com_filtros()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_retorno_com_filtros'] = self.get_url_com_filtros()
        return context


class FiltroListViewMixin(FiltroContextMixin):
    """Mixin para ListView - salva os filtros automaticamente."""
    def get(self, request, *args, **kwargs):
        self.salvar_filtros_na_sessao()
        return super().get(request, *args, **kwargs)


class FiltroFormViewMixin(FiltroContextMixin):
    """Mixin para CreateView/UpdateView."""
    pass


class FiltroDeleteViewMixin(FiltroContextMixin):
    """Mixin para DeleteView."""
    pass
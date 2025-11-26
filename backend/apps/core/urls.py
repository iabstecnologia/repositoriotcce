from django.urls import path
from .views import *

# O namespace da App para usar {% url 'core:home' %} nos templates
app_name = 'core'

urlpatterns = [
    # Rota principal (/)
    path('', HomeView.as_view(), name='home'),
    path('tcce/', TCCEView.as_view(), name='tcce'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('galeria/', GaleriaView.as_view(), name='galeria'),

    path('repositorio/', RepositorioView.as_view(), name='repositorio'),
]

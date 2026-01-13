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
    
    # ListView (Página Principal)
    path('repositorio/', RepositorioView.as_view(), name='repositorio'),
    
    # View de Download (Endpoint de Download)
    path('download/<int:pk>/', download_registro, name='registro_download'),
    
    # View de Visualização (Abre arquivo localmente)
    path('view/<int:pk>/', view_file, name='view_file'),
]

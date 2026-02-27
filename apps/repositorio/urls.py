from django.urls import path
from apps.repositorio.views.registro_views import (
	RegistroListView, RegistroDetailView, RegistroCreateView,
	RegistroUpdateView, RegistroDeleteView
)
from apps.repositorio.views.galeria_views import (
	FotoGaleriaListView, FotoGaleriaCreateView,
	FotoGaleriaUpdateView, FotoGaleriaDeleteView
)

app_name = 'repositorio'

urlpatterns = [
	# Lista de registros
	path('', RegistroListView.as_view(), name='lista'),

	# Detalhes de um registro
	path('<int:pk>/', RegistroDetailView.as_view(), name='detalhe'),

	# Criar novo registro
	path('novo/', RegistroCreateView.as_view(), name='criar'),

	# Editar registro
	path('<int:pk>/editar/', RegistroUpdateView.as_view(), name='editar'),

	# Excluir registro
	path('<int:pk>/excluir/', RegistroDeleteView.as_view(), name='excluir'),

	# Galeria
	path('galeria/', FotoGaleriaListView.as_view(), name='galeria_lista'),
	path('galeria/nova/', FotoGaleriaCreateView.as_view(), name='galeria_criar'),
	path('galeria/<int:pk>/editar/', FotoGaleriaUpdateView.as_view(), name='galeria_editar'),
	path('galeria/<int:pk>/excluir/', FotoGaleriaDeleteView.as_view(), name='galeria_excluir'),
]

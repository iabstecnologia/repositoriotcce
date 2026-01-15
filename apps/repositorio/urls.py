from django.urls import path
from apps.repositorio.views.registro_views import (
	RegistroListView, RegistroDetailView, RegistroCreateView,
	RegistroUpdateView, RegistroDeleteView
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
]

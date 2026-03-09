from django.urls import path
from apps.repositorio.views.registro_views import (
	RegistroListView, RegistroDetailView, RegistroCreateView,
	RegistroUpdateView, RegistroDeleteView, subprojetos_por_projeto_admin
)
from apps.repositorio.views.galeria_views import (
	FotoGaleriaListView, FotoGaleriaCreateView,
	FotoGaleriaUpdateView, FotoGaleriaDeleteView
)
from apps.repositorio.views.metadados_views import (
	SubprojetoListView, SubprojetoCreateView, SubprojetoUpdateView, SubprojetoDeleteView,
	TipoDocumentoListView, TipoDocumentoCreateView, TipoDocumentoUpdateView, TipoDocumentoDeleteView,
	AreaTematicaListView, AreaTematicaCreateView, AreaTematicaUpdateView, AreaTematicaDeleteView,
	TipoPublicacaoListView, TipoPublicacaoCreateView, TipoPublicacaoUpdateView, TipoPublicacaoDeleteView,
	AutorListView, AutorCreateView, AutorUpdateView, AutorDeleteView,
	TagListView, TagCreateView, TagUpdateView, TagDeleteView,
	ProjetoListView, ProjetoCreateView, ProjetoUpdateView, ProjetoDeleteView
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

	# Endpoint JSON para carregar subprojetos por projeto (gestão)
	path('api/subprojetos/', subprojetos_por_projeto_admin, name='subprojetos_por_projeto'),

	# Gestão de metadados
	path('projetos/', ProjetoListView.as_view(), name='projeto_lista'),
	path('projetos/novo/', ProjetoCreateView.as_view(), name='projeto_criar'),
	path('projetos/<int:pk>/editar/', ProjetoUpdateView.as_view(), name='projeto_editar'),
	path('projetos/<int:pk>/excluir/', ProjetoDeleteView.as_view(), name='projeto_excluir'),

	path('subprojetos/', SubprojetoListView.as_view(), name='subprojeto_lista'),
	path('subprojetos/novo/', SubprojetoCreateView.as_view(), name='subprojeto_criar'),
	path('subprojetos/<int:pk>/editar/', SubprojetoUpdateView.as_view(), name='subprojeto_editar'),
	path('subprojetos/<int:pk>/excluir/', SubprojetoDeleteView.as_view(), name='subprojeto_excluir'),

	path('tipos-documento/', TipoDocumentoListView.as_view(), name='tipodocumento_lista'),
	path('tipos-documento/novo/', TipoDocumentoCreateView.as_view(), name='tipodocumento_criar'),
	path('tipos-documento/<int:pk>/editar/', TipoDocumentoUpdateView.as_view(), name='tipodocumento_editar'),
	path('tipos-documento/<int:pk>/excluir/', TipoDocumentoDeleteView.as_view(), name='tipodocumento_excluir'),

	path('areas-tematicas/', AreaTematicaListView.as_view(), name='areatematica_lista'),
	path('areas-tematicas/nova/', AreaTematicaCreateView.as_view(), name='areatematica_criar'),
	path('areas-tematicas/<int:pk>/editar/', AreaTematicaUpdateView.as_view(), name='areatematica_editar'),
	path('areas-tematicas/<int:pk>/excluir/', AreaTematicaDeleteView.as_view(), name='areatematica_excluir'),

	path('tipos-publicacao/', TipoPublicacaoListView.as_view(), name='tipopublicacao_lista'),
	path('tipos-publicacao/novo/', TipoPublicacaoCreateView.as_view(), name='tipopublicacao_criar'),
	path('tipos-publicacao/<int:pk>/editar/', TipoPublicacaoUpdateView.as_view(), name='tipopublicacao_editar'),
	path('tipos-publicacao/<int:pk>/excluir/', TipoPublicacaoDeleteView.as_view(), name='tipopublicacao_excluir'),

	path('autores/', AutorListView.as_view(), name='autor_lista'),
	path('autores/novo/', AutorCreateView.as_view(), name='autor_criar'),
	path('autores/<int:pk>/editar/', AutorUpdateView.as_view(), name='autor_editar'),
	path('autores/<int:pk>/excluir/', AutorDeleteView.as_view(), name='autor_excluir'),

	path('tags/', TagListView.as_view(), name='tag_lista'),
	path('tags/nova/', TagCreateView.as_view(), name='tag_criar'),
	path('tags/<int:pk>/editar/', TagUpdateView.as_view(), name='tag_editar'),
	path('tags/<int:pk>/excluir/', TagDeleteView.as_view(), name='tag_excluir'),

	# Galeria
	path('galeria/', FotoGaleriaListView.as_view(), name='galeria_lista'),
	path('galeria/nova/', FotoGaleriaCreateView.as_view(), name='galeria_criar'),
	path('galeria/<int:pk>/editar/', FotoGaleriaUpdateView.as_view(), name='galeria_editar'),
	path('galeria/<int:pk>/excluir/', FotoGaleriaDeleteView.as_view(), name='galeria_excluir'),
]

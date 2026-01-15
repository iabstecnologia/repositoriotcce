from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Painel administrativo do Django
    path('admin/', admin.site.urls),

    # URLs do core (website público)
    path('', include('apps.core.urls')),
    
    # URLs do repositório (gestão de registros)
    path('gestao/', include('apps.repositorio.urls')),
]

# Configuração para servir arquivos de mídia e estáticos em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Em desenvolvimento, o Django serve arquivos estáticos. Em produção, Whitenoise/S3 faz isso.
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
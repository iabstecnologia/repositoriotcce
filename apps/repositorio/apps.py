from django.apps import AppConfig


class RepositorioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.repositorio'
    verbose_name = 'Repositorio do TCCE'

    def ready(self):
        from apps.repositorio import signals

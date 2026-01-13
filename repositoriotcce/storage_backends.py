from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


# Este backend será usado para arquivos de MÍDIA (uploads de usuários)
class MediaStorage(S3Boto3Storage):
    """
    Backend customizado para arquivos de Mídia (uploads).
    Define o prefixo (location) e a URL base.
    """
    # Define o prefixo dentro do bucket S3 (Ex: 'media/documentos/repositorio/')
    location = settings.AWS_LOCATION

    # Define a URL base que será usada no campo FileField.url
    custom_domain = settings.AWS_S3_CUSTOM_DOMAIN

    # Garante que os arquivos sejam tratados como MÍDIA (uploads)
    file_overwrite = settings.AWS_S3_FILE_OVERWRITE

    # Garante que os arquivos sejam lidos via HTTP/HTTPS (se público)
    default_acl = 'public-read'

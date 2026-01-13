import os
import environ
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------
# CONFIGURAÇÕES DO ENV E LEITURA DE VARIÁVEIS
# --------------------------------------------------------------------------

# Instancia o environ e lê o arquivo .env, se existir, na raiz do projeto (repositoriotcce/)
env = environ.Env(
    # Define as variáveis de ambiente e seus tipos/defaults
    DEBUG=(bool, False),
    SECRET_KEY=(str, 'insecure-default-key-for-development'),
    AWS_LOCATION=(str, 'media'),
    SECURE_SSL_REDIRECT=(bool, True)
)

# Define o caminho para o arquivo .env (DEVE estar na raiz: repositoriotcce/.env)
env_file = os.path.join(BASE_DIR, '.env')

# Lê o arquivo .env se ele existir
if os.path.exists(env_file):
    env.read_env(str(env_file))

# --------------------------------------------------------------------------
# CONFIGURAÇÕES
# --------------------------------------------------------------------------

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'] if DEBUG else [])
SECURE_SSL_REDIRECT = env('SECURE_SSL_REDIRECT')

# --------------------------------------------------------------------------
# APLICAÇÕES
# --------------------------------------------------------------------------

# Apps Padrão do Django
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Apps de Terceiros
THIRD_PARTY_APPS = [
    'django_cleanup.apps.CleanupConfig',  # Para remover arquivos de mídia ao deletar modelos
    'storages',  # Necessário para o S3
]

# Apps Modulares
LOCAL_APPS = [
    'apps.core.apps.CoreConfig',  # Website
    'apps.accounts.apps.AccountsConfig',  # Gerenciamento de usuários
    'apps.repositorio.apps.RepositorioConfig',  # O acervo/documentos principais
    # 'apps.search.apps.SearchConfig',  # Motor de busca e facetas
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

AUTH_USER_MODEL = 'accounts.User'

# --------------------------------------------------------------------------
# MIDDLEWARES
# --------------------------------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'repositoriotcce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Caminho global para templates: www/templates
        'DIRS': [os.path.join(BASE_DIR, 'www/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'repositoriotcce.wsgi.application'
ASGI_APPLICATION = 'repositoriotcce.asgi.application'

# --------------------------------------------------------------------------
# BANCO DE DADOS (PostgreSQL)
# --------------------------------------------------------------------------
# Lê a URL de conexão do PostgreSQL (ou SQLite padrão se não for definido)
DATABASES = {
    'default': env.db(
        'DATABASE_URL',
        default='sqlite:///db.sqlite3'
    )
}

# --------------------------------------------------------------------------
# VALIDACAO DE SENHA
# --------------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# --------------------------------------------------------------------------
# INTERNACIONALIZAÇÃO
# --------------------------------------------------------------------------

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# --------------------------------------------------------------------------
# CONFIGURAÇÃO DE ARQUIVOS ESTÁTICOS (CSS, JS, Imagens do Template)
# --------------------------------------------------------------------------

STATIC_URL = '/static/'
# Onde o Django coleta os arquivos estáticos: www/static
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Diretórios adicionais para arquivos estáticos: www/static
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "www/static/"),
]

# Configura para usar S3 para arquivos ESTÁTICOS (apenas para o comando collectstatic)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

# -----------------------------------------------------------------------------------------
# CONFIGURAÇÃO DE ARQUIVOS DE MÍDEA (MEDIA - Uploads de Usuários/Documentos) AWS S3 Config
# -----------------------------------------------------------------------------------------

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_FILE_OVERWRITE = True
AWS_LOCATION = env('AWS_LOCATION')

# URL base do S3
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# URL de Mídia (aponta para o S3)
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/"
# Root de Mídia (Apenas para fallback ou referência, se necessário)
MEDIA_ROOT = os.path.join(BASE_DIR, 'www/media')

# Configura o S3 como backend de armazenamento padrão para arquivos de MÍDIA
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'repositoriotcce.storage_backends.MediaStorage'

AWS_FILE_PATH_ROOT = env('AWS_FILE_PATH_ROOT')

# Define configurações de cache, cabeçalhos, etc.
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

# --------------------------------------------------------------------------
# CONFIGURAÇÕES DE SEGURANÇA (Geralmente em produção)
# --------------------------------------------------------------------------

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# --------------------------------------------------------------------------
# Outras Configurações
# --------------------------------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import os
from pathlib import Path

# Importa o módulo environ
import environ

# Define o diretório base do projeto (repositoriotcce/backend/)
# Usamos .parent.parent para subir para a raiz do projeto (repositoriotcce/)
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------
# CONFIGURAÇÕES DO ENV E LEITURA DE VARIÁVEIS
# --------------------------------------------------------------------------

# Instancia o environ e lê o arquivo .env, se existir, na raiz do projeto (repositoriotcce/)
env = environ.Env(
    # Define as variáveis de ambiente e seus tipos/defaults
    DEBUG=(bool, False),
    SECRET_KEY=(str, 'insecure-default-key-for-development'),
)

# Define o caminho para o arquivo .env (DEVE estar na raiz: repositoriotcce/.env)
env_file = BASE_DIR.parent / '.env'

# Lê o arquivo .env se ele existir
if os.path.exists(env_file):
    env.read_env(str(env_file))

# --------------------------------------------------------------------------
# CONFIGURAÇÕES
# --------------------------------------------------------------------------

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'] if DEBUG else [])

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
    # Adicionar o Whitenoise para servir arquivos estáticos de forma eficiente
    'whitenoise.runserver_nostatic',
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
    # Adicionar Whitenoise para servir arquivos estáticos comprimidos e em cache
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Caminho global para templates: repositoriotcce/backend/templates
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.asgi.application'

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
USE_TZ = True

# --------------------------------------------------------------------------
# CONFIGURAÇÃO DE ARQUIVOS ESTÁTICOS (CSS, JS, Imagens do Template)
# --------------------------------------------------------------------------

STATIC_URL = '/static/'
# Onde o Django coleta os arquivos estáticos: repositoriotcce/backend/staticfiles
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Diretórios adicionais para arquivos estáticos: repositoriotcce/frontend/static
STATICFILES_DIRS = [
    BASE_DIR.parent / 'frontend' / 'static',
]

# --------------------------------------------------------------------------
# CONFIGURAÇÃO DE ARQUIVOS DE MÍDEA (Uploads de Usuários/Documentos) - S3
# --------------------------------------------------------------------------

# URL de Mídia (para S3)
MEDIA_URL = '/media/'
# Root de Mídia: repositoriotcce/backend/media
MEDIA_ROOT = BASE_DIR / 'media'

# Se DEBUG for False, assume que estamos em produção e usa S3
if not DEBUG:
    # ------------------
    # AWS S3 Config
    # ------------------
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')

    # Configura o S3 como backend de armazenamento padrão para arquivos de MÍDIA
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    # URL pública base do bucket
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Configura para usar S3 para arquivos ESTÁTICOS também em produção
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

    # Define configurações de cache, cabeçalhos, etc.
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    # Configura para usar o protocolo HTTPS
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', default=True)
else:
    # Em ambiente de desenvolvimento, usa o sistema de arquivos local
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# --------------------------------------------------------------------------
# Outras Configurações
# --------------------------------------------------------------------------

# Define o tipo de chave primária padrão
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

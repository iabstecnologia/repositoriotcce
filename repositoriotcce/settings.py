import environ
from pathlib import Path
from decouple import config, Csv
import os

# --------------------------------------------------------------------------
# Configuração de ambiente
# --------------------------------------------------------------------------        
env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()  # Lê o arquivo .env na raiz do projeto

BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------
# CONFIGURAÇÕES
# --------------------------------------------------------------------------

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'] if DEBUG else [])
# ALLOWED_HOSTS = ['192.168.3.92']
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
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
        'CONN_MAX_AGE': 60,
    }
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
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    BASE_DIR / 'www/static',
]

# -----------------------------------------------------------------------------------------
# CONFIGURAÇÃO DE ARQUIVOS DE MÍDEA (MEDIA - Uploads de Usuários/Documentos)
# -----------------------------------------------------------------------------------------

# Tenta ler as configurações AWS (opcionais para desenvolvimento)
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default='')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default='')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', default='')

MEDIA_URL = '/media/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
WHITENOISE_MAX_AGE = 31536000

# Root de Mídia (usado para armazenamento local)
MEDIA_ROOT = os.path.join(BASE_DIR, 'www/media')

# --------------------------------------------------------------------------
# CONFIGURAÇÕES DE SEGURANÇA (Geralmente em produção)
# --------------------------------------------------------------------------

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# --------------------------------------------------------------------------
# Outras Configurações
# --------------------------------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Segurança de Cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SAMESITE = 'Lax'

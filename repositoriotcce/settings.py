import os
from pathlib import Path
import environ # Usaremos apenas este para tudo

# 1. Inicialização do Ambiente
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(
    DEBUG=(bool, False),
    SECURE_SSL_REDIRECT=(bool, False),
)

# Lê o arquivo .env se ele existir
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# --------------------------------------------------------------------------
# CONFIGURAÇÕES BÁSICAS
# --------------------------------------------------------------------------
SECRET_KEY = env('SECRET_KEY', default='chave-secreta-padrao-apenas-dev')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['127.0.0.1', 'localhost'])

# --------------------------------------------------------------------------
# BANCO DE DADOS (PostgreSQL)
# --------------------------------------------------------------------------
# A forma mais inteligente: usa DATABASE_URL se existir, senão monta manualmente
if env('DATABASE_URL', default=None):
    DATABASES = {
        'default': env.db()
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('DB_NAME', default='repositoriotcce'),
            'USER': env('DB_USER', default='repositoriotcce'),
            'PASSWORD': env('DB_PASSWORD', default='repositoriotcce'),
            'HOST': env('DB_HOST', default='localhost'),
            'PORT': env('DB_PORT', default='5432'),
            'CONN_MAX_AGE': 60,
        }
    }

# --------------------------------------------------------------------------
# APLICAÇÕES E MIDDLEWARES
# --------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'django_cleanup.apps.CleanupConfig',
    'storages',
]

LOCAL_APPS = [
    'apps.core.apps.CoreConfig',
    'apps.accounts.apps.AccountsConfig',
    'apps.repositorio.apps.RepositorioConfig',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # WhiteNoise logo abaixo do Security
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --------------------------------------------------------------------------
# TEMPLATES
# --------------------------------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Caminho global para seus templates customizados
        'DIRS': [os.path.join(BASE_DIR, 'www/templates')],
        'APP_DIRS': True, # Permite que o Django procure templates dentro das pastas das apps
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

# --------------------------------------------------------------------------
# SEGURANÇA INTELIGENTE
# --------------------------------------------------------------------------
# Se DEBUG for True, desativa redirecionamentos HTTPS para evitar o erro que você teve
SECURE_SSL_REDIRECT = env('SECURE_SSL_REDIRECT') if not DEBUG else False
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

# --------------------------------------------------------------------------
# ARQUIVOS ESTÁTICOS E MÍDIA
# --------------------------------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'www/static')]

# Gerenciamento de Mídia Local vs Cloud (S3)
if env('AWS_ACCESS_KEY_ID', default=''):
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
else:
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'www/media')

# Outras configurações padrão mantidas...
ROOT_URLCONF = 'repositoriotcce.urls'
WSGI_APPLICATION = 'repositoriotcce.wsgi.application'
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = USE_L10N = USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.User'
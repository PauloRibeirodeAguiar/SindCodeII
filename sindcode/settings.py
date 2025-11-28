from pathlib import Path
import os

# --------------------------
# BASE DIR
# --------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------
# SEGURANÇA
# --------------------------
SECRET_KEY = 'sua_chave_secreta_aqui'  # Troque pela sua chave real
DEBUG = True  # False em produção
ALLOWED_HOSTS = []  # Adicione o domínio quando publicar

# --------------------------
# APPS INSTALADOS
# --------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # seu app principal
]

# --------------------------
# MIDDLEWARE
# --------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # ESSENCIAL
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --------------------------
# URLS
# --------------------------
ROOT_URLCONF = 'sindcode.urls'

# --------------------------
# TEMPLATES
# --------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'core', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Necessário para request.user
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --------------------------
# WSGI
# --------------------------
WSGI_APPLICATION = 'sindcode.wsgi.application'

# --------------------------
# BANCO DE DADOS (SQLite padrão)
# --------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --------------------------
# SENHAS
# --------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# --------------------------
# INTERNACIONALIZAÇÃO
# --------------------------
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# --------------------------
# ARQUIVOS ESTÁTICOS
# --------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'core', 'static')]

# --------------------------
# ARQUIVOS DE MÍDIA
# --------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# --------------------------
# LOGIN / LOGOUT
# --------------------------
LOGIN_URL = 'login'           # Redireciona se não estiver logado
LOGIN_REDIRECT_URL = 'home'   # Redireciona após login
LOGOUT_REDIRECT_URL = 'login' # Redireciona após logout

# --------------------------
# DEFAULT AUTO FIELD
# --------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

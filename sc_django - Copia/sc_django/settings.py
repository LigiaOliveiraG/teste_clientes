import os
from pathlib import Path
import dj_database_url


DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3')
}

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Segurança (mude para True em produção)
DEBUG = True
SECRET_KEY = 'sua-chave-secreta-aqui'  # Troque por uma chave segura em produção
ALLOWED_HOSTS = ['*']

# Aplicações instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'cadastro',  # Sua aplicação de cadastro
]

# Middlewares padrão do Django
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sc_django.urls'

# Configuração dos templates (procura também em cadastro/templates/)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Usamos apenas os templates das apps
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

WSGI_APPLICATION = 'sc_django.wsgi.application'

# Banco de dados SQLite (você pode mudar depois para PostgreSQL, etc)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Validações padrão de senha
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]

# Configurações de idioma e fuso horário
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Configurações dos arquivos estáticos (CSS, JS, imagens)
STATIC_URL = '/static/'

# Pasta onde ficam os arquivos estáticos do projeto (ex: CSS, JS)
STATICFILES_DIRS = [
    BASE_DIR / "static",  # sua pasta static na raiz do projeto
]

# Pasta onde os arquivos estáticos serão coletados para produção (não deve ser a mesma que STATICFILES_DIRS)
STATIC_ROOT = BASE_DIR / "staticfiles"  # normalmente 'staticfiles' ou outro nome diferente

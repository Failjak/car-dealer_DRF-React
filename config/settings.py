from pathlib import Path
import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "apps"))

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-^3tnhm6i(k1#c0g17hehw-l$2ms!=271i3db!2zibfz(sfbt##')

DEBUG = int(os.environ.get('DEBUG', default=1))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1 0.0.0.0 localhost').split(' ')


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'apps.registration',
    'apps',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
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
        'DIRS': [],
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

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'sqlite3.db',                      # Or path to database file if using sqlite3.
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE", 'django.db.backends.postgresql'),
        "NAME": os.environ.get("DB_NAME", 'dealership'),
        "USER": os.environ.get("DB_USER", 'postgres'),
        "PASSWORD": os.environ.get("DB_USER_PASS", 'postgres'),
        "HOST": os.environ.get("DB_HOST", "0.0.0.0"),
        "PORT": os.environ.get("DB_PORT", "5445"),
    }
}

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR + "/staticfiles/"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    # "DEFAULT_FILTER_BACKENDS": (
        # "JinglePay.django_filter_extended.DjangoFilterBackendExtended",
        # 'django_filters.rest_framework.DjangoFilterBackend',
        # 'rest_framework.filters.OOPTIONSrderingFilter',
    # ),
    # "EXCEPTION_HANDLER": "apps.common.errors.utils.rest_framework_exception_handler",
}

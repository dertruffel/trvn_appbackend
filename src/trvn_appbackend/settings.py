from pathlib import Path
import os
import dj_database_url
from decouple import config
from datetime import timedelta
from corsheaders.defaults import default_headers


# DEBUG = config('DEBUG', default=False, cast=bool)
DEBUG = True
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config('SECRET_KEY', default='django-insecure-lb(#!ebof#o-ngp-izg12-nhy2@_jm@hs(^41mg!*oe7=9!m^t')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')
# AUTH_USER_MODEL = 'accounts.User'
QUERYDEBUG = True



# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    #local
    'accounts',
    'frontpages',
    'docs.apps.DocsConfig',
    #

    #external
    'bootstrapform',
    'rest_framework',
    'corsheaders',
    'storages',
    'channels',
    'tinymce',
    'adminsortable2',
    'rest_framework_recursive',
    'drf_multiple_model',
    'drf_spectacular',
    'rest_framework.authtoken',
    #
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'trvn_appbackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'trvn_appbackend.wsgi.application'
ASGI_APPLICATION = 'trvn_appbackend.asgi.application'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = list(default_headers) + [

]



CORS_ALLOW_CREDENTIALS = True

DATABASES = {'default': dj_database_url.config(conn_max_age=600)}





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
SITE_ID=1
LANGUAGE_CODE = 'en-us'
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TIME_ZONE = 'CET'

USE_I18N = True

USE_TZ = True

STATIC_URL = config('CDN_HOSTNAME', default='') + '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = config('CDN_HOSTNAME', default='') + '/assets/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'assets')

# add assets route
STATICFILES_DIRS += (
    os.path.join(BASE_DIR, 'assets'),
)

ACCOUNT_USER_MODEL_USERNAME_FIELD = None


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'PAGE_SIZE': 10,
    'ORDERING_PARAM': 'ordering',
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/minute',
    },
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}
BASE_URL = config('BASE_URL', default='http://localhost:8001')
SPECTACULAR_SETTINGS = {
    'TITLE': 'TRVN App API',
    'DESCRIPTION': 'TRVN API',
    'VERSION': '0.1.0',
    'SERVE_INCLUDE_SCHEMA': True,
    'SERVE_PUBLIC': True,
    'SERVE_URLCONF': 'config.urls',
    'SERVERS': [
        {
            'url': BASE_URL,
            'description': 'Server',
        },
    ],
    'SCHEMA_PATH_PREFIX': '/api',
    'DEFAULT_GENERATOR_CLASS': 'drf_spectacular.generators.SchemaGenerator',
    # OTHER SETTINGS
}

JWT_AUTH = {
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60 * 24),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=60 * 24 * 7),
    'ROTATE_REFRESH_TOKENS': True,
    'USER_ID_FIELD': 'jwt_secret',
}

# Documentation configuration
SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'DISPLAY_OPERATION_ID': False,
    'OPERATIONS_SORTER': 'method',
    'SECURITY_DEFINITIONS': {
        'BearerToken': {
            'scheme': 'bearer',
            'type': 'http'
        }
    },
}
FRONT_HOSTNAME = config('FRONT_HOSTNAME', default='https://localhost.8001/')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = config('APP_EMAIL_HOST', default='')
EMAIL_PORT = config('APP_EMAIL_PORT', default=587)
EMAIL_HOST_USER = config('APP_EMAIL_HOST_USER', default='')
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = config('APP_EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = config('APP_EMAIL_USE_TLS', default=True)
EMAIL_TIMEOUT = config('APP_EMAIL_TIMEOUT', default=30)

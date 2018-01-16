"""
Django Boilerplate settings
"""
###
# Libraries
###
import os
import requests

import dj_database_url
import dotenv
from s3_environ import S3Environ

###
# Get data from .env file
###
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv.read_dotenv(os.path.join(BASE_DIR, '.env'))
ENVIRONMENT = os.environ.get('ENVIRONMENT')
LOAD_ENVS_FROM_FILE = True if os.environ.get('LOAD_ENVS_FROM_FILE', False) == 'True' else False

env_file = 'envs-production.json' if ENVIRONMENT == 'production' else 'envs-staging.json'
if not LOAD_ENVS_FROM_FILE:
    S3Environ(bucket='bucket-env', key=env_file)
    print("Loading envs from S3: {0}".format(env_file))

###
# Security
###
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = ENVIRONMENT == 'development' or os.environ.get('DEBUG', False)

ALLOWED_HOSTS = [
    '.us-west-2.elb.amazonaws.com',
    '.compute-1.amazonaws.com',
    'localhost',
]

EC2_PRIVATE_IP = None
try:
    EC2_PRIVATE_IP = requests.get(
        'http://169.254.169.254/latest/meta-data/local-ipv4',
        timeout=0.01,
    ).text
except requests.exceptions.RequestException:
    pass

if EC2_PRIVATE_IP:
    ALLOWED_HOSTS.append(EC2_PRIVATE_IP)

###
# Application definition
###
INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Rest Framework
    'rest_framework',
    'rest_framework.authtoken',

    # Cors
    'corsheaders',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'

###
# Database
###
DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}
DATABASES['default']['ATOMIC_REQUESTS'] = True

###
# Internationalization
###
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

###
# Static Files
###
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

###
# Rest Framework
###
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20
}

###
# Authentication
###
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

###
# CORS
###
CORS_ORIGIN_ALLOW_ALL = True

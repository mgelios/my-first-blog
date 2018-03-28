from .base import *

MG_APP_LOCATION = 'prod'

DEBUG=False

SECRET_KEY = 'prod secret key'

SECURE_SSL_REDIRECT = True

INSTALLED_APPS = (
    'django.db.models',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'rest_framework',
    'rest_framework.authtoken',
    'blog',
    'landing',
    'dashboard',
    'todo',
    'bots',
)

TELEGRAM_BOT_ALLOWED = True

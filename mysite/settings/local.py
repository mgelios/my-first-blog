from .base import *

MG_APP_LOCATION = 'local'

DEBUG = True

SECRET_KEY = 'local secret key'

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

TELEGRAM_BOT_ALLOWED = False

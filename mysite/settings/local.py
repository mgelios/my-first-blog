from .base import *

DEBUG = True

SECRET_KEY = 'local secret key'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'blog',
    'landing',
    'dashboard',
    'django_telegrambot',
)

DJANGO_TELEGRAMBOT = {
    'MODE': 'POLLING',
    'WEBHOOK_SITE': 'localhost',
    'BOTS': [{
        'TOKEN': '460933242:AAEh67xQVBeT37EwN84iudv80tbYBsOY1QA'
    }]
}
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
    'blog',
    'landing',
    'dashboard',
    'todo',
    'bots',
    # 'django_telegrambot',
)

TELEGRAM_BOT_ALLOWED = True

# DJANGO_TELEGRAMBOT = {
#     'MODE': 'WEBHOOK',
#     'WEBHOOK_SITE': 'https://mgelios.pythonanywhere.com',
#     'WEBHOOK_PREFIX': '/telegrambot',
#     'WEBHOOK_CERTIFICATE': '',
#     'BOTS': [{
#         'TOKEN': '460933242:AAEh67xQVBeT37EwN84iudv80tbYBsOY1QA'
#     }]
# }
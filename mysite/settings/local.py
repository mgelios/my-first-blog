from .base import *

MG_APP_LOCATION = 'local'

DEBUG = True

SECRET_KEY = 'local secret key'

INSTALLED_APPS = (
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

TELEGRAM_BOT_ALLOWED = False

# DJANGO_TELEGRAMBOT = {
#     'MODE': 'POLLING',
#     'WEBHOOK_SITE': 'localhost',
#     'BOTS': [{
#         'TOKEN': '460933242:AAEh67xQVBeT37EwN84iudv80tbYBsOY1QA'
#     }]
# }
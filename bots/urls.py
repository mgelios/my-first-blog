from django.conf.urls import url
from django.urls import path, re_path, include

from . import views

urlpatterns = [
    url(r'^bots/telegram/460933242:AAEh67xQVBeT37EwN84iudv80tbYBsOY1QA/$', views.telegram_bot, name='telegram_bot'),
]
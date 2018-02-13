from django.conf.urls import url
from django.urls import path, re_path, include

from . import views

urlpatterns = [
    url(r'^bots/telegram/$', views.telegram_bot, name='telegram_bot'),
]
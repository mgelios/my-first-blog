from django.conf.urls import url
from . import views
import telegrambot
from django.conf.urls import include

urlpatterns = [
    url(r'^dashboard/$', views.dash_list, name='dash_list'),
    url(r'^telegrambot/', include('telegrambot.urls', namespace="telegrambot")),
]


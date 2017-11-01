from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^dashboard/$', views.dash_list, name='dash_list'),
#    url(r'^', include('django_telegrambot.urls')),
]


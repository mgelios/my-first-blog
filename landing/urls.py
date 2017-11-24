from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.apps_list, name='apps_list'),
    url(r'^landing/messages/$', views.messages, name='messages'),
]
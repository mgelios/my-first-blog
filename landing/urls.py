from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.apps_list, name='apps_list'),
    url(r'^landing/messages/$', views.secret_message_list, name='secret_message_list'),
    url(r'^landing/about/$', views.info_about, name='info_about'),
    url(r'^landing/register/$', views.register, name='register'),
    url(r'^landing/greeting/$', views.show_greeting, name='show_greeting'),
]
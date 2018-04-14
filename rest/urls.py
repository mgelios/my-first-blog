from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/v1/token/$', views.obtain_token, name='obtain_token'),
    url(r'^api/v1/weather/$', views.obtain_weather, name='obtain_weather'),
    url(r'^api/v1/currency/$', views.obtain_currencies, name='obtain_currencies'),
]
from django.conf.urls import url
from django.urls import path, re_path, include

from . import views

urlpatterns = [
    url(r'^dashboard/weather/$', views.weather_info, name='weather_info'),
    url(r'^dashboard/currencies/$', views.currency_info, name='currency_info'),
    url(r'^dashboard/crypto_currencies/$', views.crypto_currency_info, name='crypto_currency_info'),
    url(r'^dashboard/events/$', views.deb_by_events_info, name='deb_by_events_info'),
    url(r'^dashboard/news/$', views.radiot_news, name='radiot_news'),
    url(r'^dashboard/utilities/list/$', views.utilities_list, name='utilities_list'),
]


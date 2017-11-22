from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^dashboard/weather/$', views.weather_info, name='weather_info'),
    url(r'^dashboard/currencies/$', views.currency_info, name='currency_info'),
    url(r'^', include('django_telegrambot.urls')),
    url(r'^viber/mgbot$', views.viber_mgbot, name='viber_mgbot'),
]


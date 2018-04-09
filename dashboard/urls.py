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
    url(r'^dashboard/utilities/new/$', views.utilities_create, name='utilities_create'),
    url(r'^dashboard/utilities/update/(?P<pk>\d+)$', views.utilities_update, name='utilities_update'),
    url(r'^dashboard/utilities/delete/(?P<pk>\d+)$', views.utilities_delete, name='utilities_delete'),
    url(r'^dashboard/living_place/new/$', views.living_place_create, name='living_place_create'),
    url(r'^dashboard/living_place/update/(?P<pk>\d+)$', views.living_place_update, name='living_place_update'),
    url(r'^dashboard/living_place/delete/(?P<pk>\d+)$', views.living_place_delete, name='living_place_delete'),
    url(r'^dashboard/expenses/list/$', views.expenses_list, name='expenses_list'),
    url(r'^dashboard/expenses/new/$', views.expenses_record_create, name='expenses_record_create'),
    url(r'^dashboard/expenses/update/(?P<pk>\d+)$', views.expenses_record_update, name='expenses_record_update'),
    url(r'^dashboard/expenses/delete/(?P<pk>\d+)$', views.expenses_record_delete, name='expenses_record_delete'),
    url(r'^dashboard/expenses_category/new/$', views.expenses_category_create, name='expenses_category_create'),
    url(r'^dashboard/expenses_category/update/(?P<pk>\d+)$', views.expenses_category_update, name='expenses_category_update'),
    url(r'^dashboard/expenses_category/delete/(?P<pk>\d+)$', views.expenses_category_delete, name='expenses_category_delete'),
    url(r'^dashboard/income/new/$', views.income_record_create, name='income_record_create'),
    url(r'^dashboard/income/update/(?P<pk>\d+)$', views.income_record_update, name='income_record_update'),
    url(r'^dashboard/income/delete/(?P<pk>\d+)$', views.income_record_delete, name='income_record_delete'),
]


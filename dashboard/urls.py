from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/$', views.dash_list, name='dash_list'),
]
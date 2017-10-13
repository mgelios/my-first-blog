from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.apps_list, name='apps_list'),
]
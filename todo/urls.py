from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^todo/$', views.action_list, name='action_list'),
    url(r'^todo/task/new/$', views.create_action, name='create_action'),
    url(r'^todo/category/new/', views.create_action_category, name='create_action_category'),
    url(r'^todo/category/(?P<pk>\d+)$',views.category_action_list, name='category_action_list'),
    url(r'^todo/task/(?P<pk>\d+)$',views.update_action, name='update_action'),
]
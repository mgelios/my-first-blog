from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^todo/$', views.action_list, name='action_list'),
    url(r'^todo/task/new/$', views.create_action, name='create_action'),
    url(r'^todo/task/(?P<pk>\d+)$',views.update_action, name='update_action'),
    url(r'^todo/task/delete/(?P<pk>\d+)$',views.delete_action, name='delete_action'),
    url(r'^todo/category/new/', views.create_action_category, name='create_action_category'),
    url(r'^todo/category/(?P<pk>\d+)$',views.category_action_list, name='category_action_list'),
    url(r'^todo/category/update/(?P<pk>\d+)$',views.update_action_category, name='update_action_category'),
    url(r'^todo/category/delete/(?P<pk>\d+)$',views.delete_action_category, name='delete_action_category'),
]
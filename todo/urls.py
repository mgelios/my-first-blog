from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^todo/$', views.action_list, name='action_list'),
    # url(r'^todo/task/(?P<pk>\d+)/$', views.update_action, name='update_action'),
    url(r'^todo/category/new/', views.create_action_category, name='create_action_category'),
]
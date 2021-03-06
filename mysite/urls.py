from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views

urlpatterns = [
    url(r'^api/v1/', include('rest_framework.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'', include('blog.urls')),
    url(r'', include('landing.urls')),
    url(r'', include('dashboard.urls')),
    url(r'', include('todo.urls')),
    url(r'', include('bots.urls')),
    url(r'', include('rest.urls')),
]

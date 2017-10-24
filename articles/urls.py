from django.conf.urls import include, url
from django.contrib.auth import views

urlpatterns = [
    url(r'^articles/api/v0/', include('api_v0.urls')),
]

from django.contrib import admin
from .models import Weather, WeatherForecast

admin.site.register(Weather)
admin.site.register(WeatherForecast)



from django.db import models
from django.utils import timezone

class Currency(models.Model):
    scale = models.FloatField(default=0.0)

class Weather(models.Model):
    main_info = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    icon_name = models.CharField(max_length=200)

    temperature = models.IntegerField(default=0)
    humidity = models.IntegerField(default=0)
    pressure = models.IntegerField(default=0)
    temperature_min = models.IntegerField(default=0)
    temperature_max = models.IntegerField(default=0)

    wind_speed = models.FloatField(default=0.0)
    wind_deg = models.FloatField(default=0.0)

    sunrise = models.DateTimeField(default=timezone.now)
    sunset = models.DateTimeField(default=timezone.now)


class WeatherForecast(models.Model):
    temperature = models.IntegerField(default=0)
    temperature_min = models.IntegerField(default=0)
    temperature_max = models.IntegerField(default=0)
    pressure = models.IntegerField(default=0)
    humidity = models.IntegerField(default=0)

    main_info = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    icon_name = models.CharField(max_length=200)

    wind_speed = models.FloatField(default=0.0)
    wind_deg = models.FloatField(default=0.0)

    date_time = models.DateTimeField(default=timezone.now)


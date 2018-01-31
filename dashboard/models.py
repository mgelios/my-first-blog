from django.db import models
from django.utils import timezone

class Currency(models.Model):
    scale = models.FloatField(default=0.0)
    rate = models.FloatField(default=0.0)
    abbreviation = models.CharField(default='', max_length=200)
    last_updated = models.DateTimeField(default=timezone.now)

class CurrencyConversion(models.Model):
    value = models.FloatField(default=0.0)
    currency_from = models.CharField(default='', max_length=200)
    currency_to = models.CharField(default='', max_length=200)

class CurrencyStatistics(models.Model):
    abbreviation = models.CharField(default='', max_length=200)
    rate = models.FloatField(default=0.0)
    date = models.DateTimeField(default=timezone.now)

class Weather(models.Model):
    main_info = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200, default='')
    icon_name = models.CharField(max_length=200, default='')
    city_name = models.CharField(max_length=200, default='')
    temperature = models.IntegerField(default=0)
    humidity = models.IntegerField(default=0)
    pressure = models.IntegerField(default=0)
    visibility = models.IntegerField(default=0)
    temperature_min = models.IntegerField(default=0)
    temperature_max = models.IntegerField(default=0)
    wind_speed = models.FloatField(default=0.0)
    wind_deg = models.FloatField(default=0.0)
    sunrise = models.DateTimeField(default=timezone.now)
    sunset = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)
    date = models.DateTimeField(default=timezone.now)


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


from django.db import models
from django.utils import timezone


class RadiotArticle(models.Model):
    title = models.CharField(max_length=400, default='')
    content = models.TextField(default='')
    snippet = models.TextField(default='')
    main_pic = models.CharField(max_length=200, default='')
    link = models.CharField(max_length=200, default='')
    author = models.CharField(max_length=200, default='')
    original_ts = models.DateTimeField(default=timezone.now)
    radiot_ts = models.DateTimeField(default=timezone.now)
    feed = models.TextField(default='')
    slug = models.TextField(default='')
    comments = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    last_updated = models.DateTimeField(default=timezone.now)

class DevByEvent(models.Model):
    title = models.CharField(max_length=400, default='')
    content = models.TextField(default='')
    link = models.CharField(max_length=400, default='')
    last_updated = models.DateTimeField(default=timezone.now)

class CryptoMarket(models.Model):
    total_usd = models.IntegerField(default=0.0)
    total_usd_day_volume = models.IntegerField(default=0.0)
    active_markets = models.IntegerField(default=0.0)
    active_currencies = models.IntegerField(default=0)
    bitcoin_percent = models.FloatField(default=0.0)
    last_updated = models.DateTimeField(default=timezone.now)

class CryptoCurrency(models.Model):
    name = models.CharField(max_length=200, default='')
    symbol = models.CharField(max_length=200, default='')
    rank = models.IntegerField(default=0)
    price_usd = models.FloatField(default=0.0)
    price_btc = models.FloatField(default=0.0)
    change_24h = models.FloatField(default=0.0)

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
    requested_city = models.CharField(max_length=200, default='')
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
    city = models.CharField(max_length=200, default='')
    requested_city = models.CharField(max_length=200, default='')
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


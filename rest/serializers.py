from datetime import datetime

from rest_framework import serializers

class CryptoMarketSerializer(serializers.Serializer):
    total_usd = serializers.IntegerField(read_only=True)
    total_usd_day_volume = serializers.IntegerField(read_only=True)
    active_markets = serializers.IntegerField(read_only=True)
    active_currencies = serializers.IntegerField(read_only=True)
    bitcoin_percent = serializers.FloatField(read_only=True)
    last_updated = serializers.DateTimeField(read_only=True)

class CryptoCurrencySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200, read_only=True)
    symbol = serializers.CharField(max_length=200, read_only=True)
    rank = serializers.IntegerField(read_only=True)
    price_usd = serializers.FloatField(read_only=True)
    price_btc = serializers.FloatField(read_only=True)
    change_24h = serializers.FloatField(read_only=True)

class CurrencyStatisticsSerializer(serializers.Serializer):
    abbreviation = serializers.CharField(max_length=200, read_only=True)
    rate = serializers.FloatField(read_only=True)
    date = serializers.DateTimeField(read_only=True)

class CurrencyConversionSerializer(serializers.Serializer):
    value = serializers.FloatField(read_only=True)
    currency_from = serializers.CharField(max_length=200, read_only=True)
    currency_to = serializers.CharField(max_length=200, read_only=True)

class CurrencySerializer(serializers.Serializer):
    scale = serializers.FloatField(read_only=True)
    rate = serializers.FloatField(read_only=True)
    abbreviation = serializers.CharField(max_length=200, read_only=True)
    last_updated = serializers.DateTimeField(read_only=True)

class WeatherSerializer(serializers.Serializer):
    main_info = serializers.CharField(max_length=200, read_only=True)
    description = serializers.CharField(max_length=200, read_only=True)
    icon_name = serializers.CharField(max_length=200, read_only=True)
    city_name = serializers.CharField(max_length=200, read_only=True)
    requested_city = serializers.CharField(max_length=200, read_only=True)
    temperature = serializers.IntegerField(read_only=True)
    humidity = serializers.IntegerField(read_only=True)
    pressure = serializers.IntegerField(read_only=True)
    visibility = serializers.IntegerField(read_only=True)
    temperature_min = serializers.IntegerField(read_only=True)
    temperature_max = serializers.IntegerField(read_only=True)
    wind_speed = serializers.FloatField(read_only=True)
    wind_deg = serializers.FloatField(read_only=True)
    sunrise = serializers.DateTimeField(read_only=True)
    sunset = serializers.DateTimeField(read_only=True)
    last_updated = serializers.DateTimeField(read_only=True)
    date = serializers.DateTimeField(read_only=True)

class WeatherForecastSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=200, read_only=True)
    requested_city = serializers.CharField(max_length=200, read_only=True)
    temperature = serializers.IntegerField(read_only=True)
    temperature_min = serializers.IntegerField(read_only=True)
    temperature_max = serializers.IntegerField(read_only=True)
    pressure = serializers.IntegerField(read_only=True)
    humidity = serializers.IntegerField(read_only=True)
    main_info = serializers.CharField(max_length=200, read_only=True)
    description = serializers.CharField(max_length=200, read_only=True)
    icon_name = serializers.CharField(max_length=200, read_only=True)
    wind_speed = serializers.FloatField(read_only=True)
    wind_deg = serializers.FloatField(read_only=True)
    date_time = serializers.DateTimeField(read_only=True)

from django.db import models
from django.utils import timezone

import json
import urllib
from datetime import datetime, timezone
from dashboard.models import Weather, WeatherForecast

base_context = 'http://api.openweathermap.org/data/2.5/'
weather_suffix = 'weather'
forecast_suffix = 'forecast'
cities = ['Minsk,by' ,'Kapyl,by']
api_key = '0502d0f1f744a28dd8065598094fa1db'
units = 'metric'
lang = 'ru'
LATENCY = 600


def update_info():
    test_weather = None
    try:
        test_weather = Weather.objects.get()
    except Weather.DoesNotExist:
        test_weather = None

    if (test_weather == None):
        get_current_weather()
        get_db_forecast()
    else:
        last_updated = test_weather.last_updated
        from_last_update = (datetime.now(timezone.utc) - last_updated).total_seconds()
        if (from_last_update >= LATENCY):
            get_current_weather()
            get_db_forecast()

def forecast():
    json_content = []

    for city in cities:
        weather_query = base_context + weather_suffix + '?' + 'q=' + city + '&appid=' + api_key + '&units=' + units + '&lang=' + lang
        forecast_query = base_context + forecast_suffix + '?' + 'q=' + city + '&appid=' + api_key + '&units=' + units + '&lang=' + lang
        weather_content_raw = urllib.request.urlopen(weather_query).read().decode('utf-8')
        forecast_content_raw = urllib.request.urlopen(forecast_query).read().decode('utf-8')

        weather_content = json.loads(weather_content_raw)
        forecast_content = json.loads(forecast_content_raw)
        for item in forecast_content['list']:
            item['dt'] = datetime.fromtimestamp(item['dt'])
        json_content.append([weather_content, forecast_content])

    return json_content

def get_current_weather_raw():
    context = base_context + weather_suffix
    city = cities[0]
    query = '?' + 'q=' + city + '&appid=' + api_key + '&units=' + units + '&lang=' + lang
    json_content = urllib.request.urlopen(context + query).read().decode('utf-8')
    raw_object = json.loads(json_content)

    raw_object['sys']['sunrise'] = datetime.fromtimestamp(raw_object['sys']['sunrise'])
    raw_object['sys']['sunset'] = datetime.fromtimestamp(raw_object['sys']['sunset'])
    raw_object['dt'] = datetime.fromtimestamp(raw_object['dt'])

    return raw_object

def get_forecast_raw():
    context = base_context + forecast_suffix
    city = cities[0]
    query = '?' + 'q=' + city + '&appid=' + api_key + '&units=' + units + '&lang=' + lang
    json_content = urllib.request.urlopen(context + query).read().decode('utf-8')
    raw_list = json.loads(json_content)['list']

    for list_unit in raw_list:
        list_unit['dt'] = datetime.fromtimestamp(list_unit['dt'])

    return raw_list

def get_current_weather():
    weather_raw = get_current_weather_raw()
    default_string = ''
    default_int = -1
    default_float = -1.0

    Weather.objects.filter(main_info__isnull=False).delete()
    weather = Weather.objects.create()
    weather.main_info = weather_raw['weather'][0].get('main', default_string)
    weather.description = weather_raw['weather'][0].get('description', default_string)
    weather.icon_name = weather_raw['weather'][0].get('icon', default_string)
    weather.city_name = weather_raw.get('name', default_string)
    weather.temperature = int(weather_raw['main'].get('temp', default_int))
    weather.humidity = int(weather_raw['main'].get('humidity', default_int))
    weather.pressure = int(weather_raw['main'].get('pressure', default_int))
    weather.visibility = int(weather_raw.get('visibility', default_int))
    weather.temperature_min = int(weather_raw['main'].get('temp_min', default_int))
    weather.temperature_max = int(weather_raw['main'].get('temp_max', default_int))
    weather.wind_speed = float(weather_raw['wind'].get('speed', default_float))
    weather.wind_deg = float(weather_raw['wind'].get('deg', default_float))
    weather.sunrise = weather_raw['sys']['sunrise']
    weather.sunset = weather_raw['sys']['sunset']
    weather.date = weather_raw['dt']

    weather.save()

    return Weather.objects

def get_db_forecast():
    forecasts_raw = get_forecast_raw()
    default_string = ''
    default_int = -1
    default_float = -1.0

    WeatherForecast.objects.filter(main_info__isnull=False).delete()
    for forecast_raw in forecasts_raw:
        forecast = WeatherForecast.objects.create()

        forecast.main_info = forecast_raw['weather'][0].get('main', default_string)
        forecast.description = forecast_raw['weather'][0].get('description', default_string)
        forecast.icon_name = forecast_raw['weather'][0].get('icon', default_string)
        forecast.temperature = forecast_raw['main'].get('temp', default_int)
        forecast.temperature_min = forecast_raw['main'].get('temp_min', default_int)
        forecast.temperature_max = forecast_raw['main'].get('temp_max', default_int)
        forecast.pressure = forecast_raw['main'].get('pressure', default_int)
        forecast.humidity = forecast_raw['main'].get('humidity', default_int)
        forecast.wind_speed = forecast_raw['wind'].get('speed', default_float)
        forecast.wind_deg = forecast_raw['wind'].get('deg', default_float)
        forecast.date_time = forecast_raw['dt']

        forecast.save()

    return WeatherForecast.objects
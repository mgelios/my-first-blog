import json
import urllib
import datetime
from dashboard.models import Weather

base_context = 'http://api.openweathermap.org/data/2.5/'
weather_suffix = 'weather'
forecast_suffix = 'forecast'
cities = ['Minsk,by' ,'Kapyl,by']
api_key = '0502d0f1f744a28dd8065598094fa1db'
units = 'metric'
lang = 'ru'


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
            item['dt'] = datetime.datetime.fromtimestamp(item['dt'])
        json_content.append([weather_content, forecast_content])

    return json_content

def get_current_weather_raw():
    context = base_context + weather_suffix
    city = cities[0]
    query = '?' + 'q=' + city + '&appid=' + api_key + '&units=' + units + '&lang=' + lang
    json_content = urllib.request.urlopen(context + query).read().decode('utf-8')
    raw_object = json.loads(json_content)

    raw_object['sys']['sunrise'] = datetime.datetime.fromtimestamp(raw_object['sys']['sunrise'])
    raw_object['sys']['sunset'] = datetime.datetime.fromtimestamp(raw_object['sys']['sunset'])
    raw_object['dt'] = datetime.datetime.fromtimestamp(raw_object['dt'])

    return raw_object

def get_current_weather():
    weather_raw = get_current_weather_raw()

    Weather.objects.filter(main_info__isnull=False).delete()
    weather = Weather.objects.create()
    weather.main_info = weather_raw['weather'][0]['main']
    weather.description = weather_raw['weather'][0]['description']
    weather.icon_name = weather_raw['weather'][0]['icon']
    weather.city_name = weather_raw['name']
    weather.temperature = int(weather_raw['main']['temp'])
    weather.humidity = int(weather_raw['main']['humidity'])
    weather.pressure = int(weather_raw['main']['pressure'])
    weather.visibility = int(weather_raw['visibility'])
    weather.temperature_min = int(weather_raw['main']['temp_min'])
    weather.temperature_max = int(weather_raw['main']['temp_max'])
    weather.wind_speed = float(weather_raw['wind']['speed'])
    weather.wind_deg = float(weather_raw['wind']['deg'])
    weather.sunrise = weather_raw['sys']['sunrise']
    weather.sunset = weather_raw['sys']['sunset']
    weather.date = weather_raw['dt']

    weather.save()

    return Weather.objects
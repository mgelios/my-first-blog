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

def get_current_weather():
    json_content = []

    Weather.objects.filter(main_info__isnull=False).delete()
    weather = Weather.objects.create()
    weather.main_info = "info"
    weather.save()

    return Weather.objects
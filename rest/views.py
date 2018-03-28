from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from dashboard.models import Weather, WeatherForecast
from dashboard.models import Currency
from dashboard.models import CryptoMarket
from dashboard.models import CryptoCurrency
from dashboard.models import CurrencyConversion
from dashboard.models import CurrencyStatistics
from dashboard.models import RadiotArticle

from dashboard.dashes.news import Radiot
from dashboard.dashes.weather import OpenWeather
from dashboard.dashes.currency import NBRBCurrency
from dashboard.dashes.crypto_currency import CryptoCurrencyInfo

from .serializers import WeatherSerializer, WeatherForecastSerializer


@api_view()
@login_required
def obtain_token(request):
    token = Token.objects.get_or_create(user=request.user)
    return Response({'token': token[0].key})


@api_view()
def obtain_weather(request):
    requested_city = 'minsk'
    OpenWeather.update_info(requested_city)
    weather = Weather.objects.filter(requested_city=requested_city)[0]
    weather = WeatherSerializer(weather).data
    forecast_db = WeatherForecast.objects.filter(city='Minsk').order_by('date_time')
    forecast = []
    for forecast_item in forecast_db:
        forecast.append(WeatherForecastSerializer(forecast_item).data)
    return Response({'weather': weather, 'forecast': forecast})
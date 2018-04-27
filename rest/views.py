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
from .serializers import CurrencySerializer, CurrencyConversionSerializer, CurrencyStatisticsSerializer


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

@api_view()
def obtain_currencies(request):
    NBRBCurrency.update_info()
    currencies_db = Currency.objects.filter(scale__isnull=False)
    statistics_eur_db = CurrencyStatistics.objects.filter(abbreviation='EUR').order_by('date')
    statistics_usd_db = CurrencyStatistics.objects.filter(abbreviation='USD').order_by('date')
    conversions_db = CurrencyConversion.objects.filter(value__isnull=False)
    currencies = []
    conversions = []
    statistics_usd = []
    statistics_eur = []
    for currency_db in currencies_db:
        currencies.append(CurrencySerializer(currency_db).data)
    for conversion_db in conversions_db:
        conversions.append(CurrencyConversionSerializer(conversion_db).data)
    for statistic_usd_db in statistics_usd_db:
        statistics_usd.append(CurrencyStatisticsSerializer(statistic_usd_db).data)
    for statistic_eur_db in statistics_eur_db:
        statistics_eur.append(CurrencyStatisticsSerializer(statistic_eur_db).data)
    return Response({
        'currencies': currencies, 
        'conversions': conversions, 
        'statistics_eur': statistics_eur,
        'statistics_usd': statistics_usd
    })

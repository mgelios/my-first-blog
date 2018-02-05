from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone

from django.http import HttpResponse

import datetime

from dashboard.dashes.weather import OpenWeather
from dashboard.dashes.currency import NBRBCurrency
from dashboard.dashes.crypto_currency import CryptoCurrencyInfo

from .models import Weather, WeatherForecast
from .models import Currency, CurrencyStatistics, CurrencyConversion
from .models import CryptoCurrency, CryptoMarket

from viberbot import Api
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.bot_configuration import BotConfiguration

from viberbot.api.viber_requests import ViberMessageRequest

bot_configuration = BotConfiguration(
    name='mgbot',
    avatar='https://pp.userapi.com/c840332/v840332973/24399/5gjeGVXaiWE.jpg',
    auth_token='46f8cbe1dee7d22a-2654d549e59d8703-5d9a149e324492c0'
)

viber = Api(bot_configuration)

def weather_info(request):
    OpenWeather.update_info()
    weather = get_object_or_404(Weather, city_name='Minsk')
    forecast = WeatherForecast.objects.filter(date_time__isnull=False).order_by('date_time')
    return render(request, 'weather.html', {'forecast': forecast, 'weather': weather})

def currency_info(request):
    NBRBCurrency.update_info()
    currencies = Currency.objects.filter(scale__isnull=False)
    statistics_eur = CurrencyStatistics.objects.filter(abbreviation='EUR').order_by('date')
    statistics_usd = CurrencyStatistics.objects.filter(abbreviation='USD').order_by('date')
    conversions = CurrencyConversion.objects.filter(value__isnull=False)
    return render(request, 'currency.html', {
        'currencies': currencies, 
        'statistics_eur': statistics_eur,
        'statistics_usd': statistics_usd,
        'conversions': conversions 
    })

def viber_mgbot(request):
    if request.method == "POST":
        viber_request = viber.parse_request(request.get_data())
        if isinstanse(viber_request, ViberMessageRequest):
            message = viber_request.message
            viber.send_message(viber_request.sender.id, [
                message
            ])
    return HttpResponse(status=200)

def crypto_currency_info(request):
    CryptoCurrencyInfo.update_info()
    crypto_currencies = CryptoCurrency.objects.order_by('rank')
    crypto_market = CryptoMarket.objects.get()
    return render(request, 'crypto_currency.html', 
        {
            'crypto_currencies': crypto_currencies,
            'crypto_market': crypto_market
        })




from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone

from django.http import HttpResponse

from dashboard.dashes.weather import OpenWeather
from dashboard.dashes.currency import NBRBCurrency
from dashboard.dashes.crypto_currency import CryptoCurrency

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
    forecasts = OpenWeather.forecast()
    return render(request, 'weather.html', {'forecasts': forecasts})

def currency_info(request):
    currencies = NBRBCurrency.get_currencies()
    statistics = NBRBCurrency.get_statistics_list()
    return render(request, 'currency.html', {'currencies': currencies, 'statistics': statistics })

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
    crypto_currencies = CryptoCurrency.get_currencies()
    return render(request, 'crypto_currency.html', {'crypto_currencies': crypto_currencies})




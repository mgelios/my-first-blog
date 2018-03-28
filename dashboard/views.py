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
from dashboard.dashes.events import DevBy
from dashboard.dashes.news import Radiot

from .models import Weather, WeatherForecast
from .models import Currency, CurrencyStatistics, CurrencyConversion
from .models import CryptoCurrency, CryptoMarket
from .models import DevByEvent
from .models import RadiotArticle
from .models import LivingPlace, UtilitiesRecord

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

def radiot_news(request):
    Radiot.update_info()
    news = RadiotArticle.objects.order_by('-radiot_ts')
    return render(request, 'news.html', {'news': news})

def deb_by_events_info(request):
    DevBy.update_info()
    events = DevByEvent.objects.order_by('last_updated')
    return render(request, 'events.html', {'events': events})

def weather_info(request):
    OpenWeather.update_info()
    weather = get_object_or_404(Weather, city_name='Minsk')
    forecast = WeatherForecast.objects.filter(city='Minsk').order_by('date_time')
    dates = []
    dates_forecast = []
    for info in forecast:
        if len(dates) == 0 or info.date_time.day != dates[len(dates) - 1]:
            dates.append(info.date_time.day)
    max_temp = -200
    min_temp = 1000
    for date in dates:
        date_min = None
        date_max = None
        for info in forecast:
            if (info.date_time.day==date and (date_min==None or date_min.temperature > info.temperature)):
                date_min = info
            if (info.date_time.day==date and (date_max==None or date_max.temperature < info.temperature)):
                date_max = info
            if (max_temp < info.temperature):
                max_temp = info.temperature
            if (min_temp > info.temperature):
                min_temp = info.temperature
        dates_forecast.append([date_min, date_max])

    print(dates)
    return render(request, 'weather.html', {'weather': weather, 'forecast': dates_forecast, 'min_temp': min_temp, 'max_temp': max_temp})

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

@login_required
def utilities_list(request):
    utilities_records = UtilitiesRecord.objects.order_by('date')
    living_places = LivingPlace.objects.order_by('last_updated')
    return render(request, 'utilities.html', 
        {
            'utilities': utilities_records,
            'living_places': living_places
        })

@login_required
def utilities_create(request):
    if request.method == 'POST':
        form = UtilityRecordForm(request.POST)
        if (form.is_valid):
            utility_record = form.save()
            utility_record.save()
            return redirect('utilities_list', pk=utility_record.place.pk)
    else:
        form = UtilityRecordForm()
        form.fields['place'].queryset = LivingPlace.objects.filter(author=request.user)
    return render(request, 'utilities_edit.html', {'form': form})

@login_required
def utilities_update(request, pk):
    utilities = get_object_or_404(UtilitiesRecord, pk=pk)
    if request.method == 'POST':
        form = UtilityRecordForm(request.POST)
        if (form.is_valid):
            utility_record = form.save()
            utility_record.save()
            return redirect('utilities_list', pk=utility_record.place.pk)
    else:
        form = UtilityRecordForm(instance=utilities)
        form.fields['place'].queryset = LivingPlace.objects.filter(author=request.user)
    return render(request, 'utilities_edit.html', {'form': form})


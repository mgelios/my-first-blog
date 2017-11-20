from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from dashboard.dashes.weather import OpenWeather
from dashboard.dashes.currency import NBRBCurrency


#Post actions section

def weather_info(request):
    forecasts = OpenWeather.forecast()
    return render(request, 'weather.html', {'forecasts': forecasts})

def currency_info(request):
    currencies = NBRBCurrency.get_currencies()
    print(currencies)
    return render(request, 'currency.html', {'currencies': currencies})



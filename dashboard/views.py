from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from dashboard.dashes.weather import OpenWeather
from dashboard.dashes.currency import NBRBCurrency


#Post actions section

def dash_list(request):
    forecasts = OpenWeather.forecast()
    currencies = NBRBCurrency.get_currencies()

    return render(request, 'weather.html', {'forecasts': forecasts, 'currencies': currencies})



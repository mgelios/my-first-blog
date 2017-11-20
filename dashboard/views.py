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
    final_string = 'Курсы валют от НБРБ: \n'
    for currency in currencies:
        final_string = final_string + '{0} {1} = {2} BYN \n'.format(currency.get('Cur_Scale'), currency.get('Cur_Abbreviation'), currency.get('Cur_OfficialRate'))
    print(final_string)
    return render(request, 'currency.html', {'currencies': currencies})



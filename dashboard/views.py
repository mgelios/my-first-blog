from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone

from django.http import HttpResponse

from datetime import datetime, timedelta

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
from .models import IncomeRecord, ExpensesRecord, ExpensesCategory

from .forms import UtilityRecordForm, LivingPlaceForm
from .forms import ExpensesCategoryForm, ExpensesRecordForm, IncomeRecordForm

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

# 
# place for utilities section
# 

@login_required
def utilities_list(request):
    utilities_records = UtilitiesRecord.objects.order_by('-date')
    living_places = LivingPlace.objects.filter(author=request.user).order_by('-last_updated')
    electricity_in_one_day = 0.0
    hot_water_in_one_day = 0.0
    cold_water_in_one_day = 0.0
    electricity_scale = 10.0
    water_scale = 100.0
    first_utilities_record = utilities_records[len(utilities_records) - 1]
    last_utilities_record = utilities_records[0]
    days = (last_utilities_record.date - first_utilities_record.date).days
    electricity_in_one_day = (last_utilities_record.electricity - first_utilities_record.electricity)
    hot_water_in_one_day = (last_utilities_record.hot_water - first_utilities_record.hot_water)
    cold_water_in_one_day = (last_utilities_record.cold_water - first_utilities_record.cold_water)
    electricity_in_one_day = electricity_in_one_day / (electricity_scale * days)
    hot_water_in_one_day = hot_water_in_one_day / (water_scale * days)
    cold_water_in_one_day = cold_water_in_one_day / (water_scale * days)
    return render(request, 'utilities.html', 
        {
            'utilities': utilities_records,
            'living_places': living_places,
            'cold_water_in_one_day' : cold_water_in_one_day,
            'hot_water_in_one_day' : hot_water_in_one_day,
            'electricity_in_one_day' : electricity_in_one_day
        })

@login_required
def utilities_create(request):
    if request.method == 'POST':
        form = UtilityRecordForm(request.POST)
        if (form.is_valid):
            utility_record = form.save()
            utility_record.save()
            return redirect('utilities_list')
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
            return redirect('utilities_list')
    else:
        form = UtilityRecordForm(instance=utilities)
        form.fields['place'].queryset = LivingPlace.objects.filter(author=request.user)
    return render(request, 'utilities_edit.html', {'form': form, 'is_update': True})

@login_required
def utilities_delete(request, pk):
    utilities = get_object_or_404(UtilitiesRecord, pk=pk)
    utilities.delete()
    return redirect('utilities_list')

@login_required
def living_place_create(request):
    if request.method == 'POST':
        form = LivingPlaceForm(request.POST)
        if (form.is_valid):
            living_place_record = form.save()
            living_place_record.author = request.user
            living_place_record.save()
            return redirect('utilities_list')
    else:
        form = LivingPlaceForm()
    return render(request, 'living_place_edit.html', {'form': form})

@login_required
def living_place_update(request, pk):
    living_place = get_object_or_404(LivingPlace, pk=pk)
    if request.method == 'POST':
        form = LivingPlaceForm(request.POST)
        if (form.is_valid):
            living_place_record = form.save()
            living_place_record.author = request.user
            living_place_record.save()
            return redirect('utilities_list')
    else:
        form = LivingPlaceForm(instance=living_place)
    return render(request, 'living_place_edit.html', {'form': form, 'is_update': True})

@login_required
def living_place_delete(request, pk):
    living_place = get_object_or_404(LivingPlace, pk=pk)
    living_place.delete()
    return redirect('utilities_list')

#
#
# expenses part
#
#

@login_required
def expenses_list(request):
    scale = 100.0
    fromDate = datetime.today() - timedelta(days=30)
    expenses_records = ExpensesRecord.objects.filter(author=request.user).filter(date__gte=fromDate).order_by('-date')
    expenses_categories = ExpensesCategory.objects.filter(author=request.user)
    income_records = IncomeRecord.objects.filter(author=request.user).filter(date__gte=fromDate).order_by('-date')
    summary = 0.0
    for expenses_record in expenses_records:
        summary = summary + expenses_record.amount
    summary = summary / scale
    category_info = []
    for expenses_category in expenses_categories:
        category_summary = 0.0
        for expenses_record in expenses_records:
            if expenses_record.category == expenses_category:
                category_summary = category_summary + expenses_record.amount
        category_summary = category_summary / scale
        category_info.append({'name': expenses_category.name, 'amount': category_summary})
    return render(request, 'expenses.html', 
        {
            'expenses': expenses_records,
            'expenses_categories': expenses_categories,
            'incomes' : income_records,
            'scale' : 100,
            'summary' : summary,
            'category_info' : category_info
        })

@login_required
def expenses_record_delete(request, pk):
    expenses_record = get_object_or_404(ExpensesRecord, pk=pk)
    expenses_record.delete()
    return redirect('expenses_list')

@login_required
def expenses_category_delete(request, pk):
    expenses_category = get_object_or_404(ExpensesCategory, pk=pk)
    expenses_category.delete()
    return redirect('expenses_list')

@login_required
def income_record_delete(request, pk):
    income_record = get_object_or_404(IncomeRecord, pk=pk)
    income_record.delete()
    return redirect('expenses_list')

@login_required
def expenses_category_create(request):
    if request.method == 'POST':
        form = ExpensesCategoryForm(request.POST)
        if (form.is_valid):
            expenses_category = form.save()
            expenses_category.author = request.user
            expenses_category.save()
            return redirect('utilities_list')
    else:
        form = ExpensesCategoryForm()
    return render(request, 'expenses_category_edit.html', {'form': form})

@login_required
def expenses_category_update(request, pk):
    expenses_category = get_object_or_404(ExpensesCategory, pk=pk)
    if request.method == 'POST':
        form = ExpensesCategoryForm(request.POST)
        if (form.is_valid):
            expenses_category_record = form.save()
            expenses_category_record.author = request.user
            expenses_category_record.save()
            return redirect('utilities_list')
    else:
        form = ExpensesCategoryForm(instance=expenses_category)
    return render(request, 'expenses_category_edit.html', {'form': form, 'is_update': True})

@login_required
def expenses_category_create(request):
    if request.method == 'POST':
        form = ExpensesCategoryForm(request.POST)
        if (form.is_valid):
            expenses_category = form.save()
            expenses_category.author = request.user
            expenses_category.save()
            return redirect('expenses_list')
    else:
        form = ExpensesCategoryForm()
    return render(request, 'expenses_category_edit.html', {'form': form})

@login_required
def expenses_category_update(request, pk):
    expenses_category = get_object_or_404(ExpensesCategory, pk=pk)
    if request.method == 'POST':
        form = ExpensesCategoryForm(request.POST)
        if (form.is_valid):
            expenses_category_record = form.save()
            expenses_category_record.author = request.user
            expenses_category_record.save()
            return redirect('expenses_list')
    else:
        form = ExpensesCategoryForm(instance=expenses_category)
    return render(request, 'expenses_category_edit.html', {'form': form, 'is_update': True})

@login_required
def expenses_record_create(request):
    if request.method == 'POST':
        form = ExpensesRecordForm(request.POST)
        if (form.is_valid):
            expenses_record = form.save()
            expenses_record.author = request.user
            expenses_record.save()
            return redirect('expenses_list')
    else:
        form = ExpensesRecordForm()
        form.fields['category'].queryset = ExpensesCategory.objects.filter(author=request.user)
    return render(request, 'expenses_record_edit.html', {'form': form})

@login_required
def expenses_record_update(request, pk):
    expenses_record = get_object_or_404(ExpensesRecord, pk=pk)
    if request.method == 'POST':
        form = ExpensesRecordForm(request.POST)
        if (form.is_valid):
            expenses_form_record = form.save()
            expenses_form_record.author = request.user
            expenses_form_record.save()
            return redirect('expenses_list')
    else:
        form = ExpensesRecordForm(instance=expenses_record)
        form.fields['category'].queryset = ExpensesCategory.objects.filter(author=request.user)
    return render(request, 'expenses_record_edit.html', {'form': form, 'is_update': True})

@login_required
def income_record_create(request):
    if request.method == 'POST':
        form = IncomeRecordForm(request.POST)
        if (form.is_valid):
            income_record = form.save()
            income_record.author = request.user
            income_record.save()
            return redirect('expenses_list')
    else:
        form = IncomeRecordForm()
    return render(request, 'income_record_edit.html', {'form': form})

@login_required
def income_record_update(request, pk):
    income_record = get_object_or_404(IncomeRecord, pk=pk)
    if request.method == 'POST':
        form = IncomeRecordForm(request.POST)
        if (form.is_valid):
            income_form_record = form.save()
            income_form_record.author = request.user
            income_form_record.save()
            return redirect('expenses_list')
    else:
        form = IncomeRecordForm(instance=expenses_record)
    return render(request, 'income_record_edit.html', {'form': form, 'is_update': True})



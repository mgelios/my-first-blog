import json
import urllib
from datetime import timedelta
from datetime import datetime

from django.shortcuts import get_object_or_404

from dashboard.models import Currency, CurrencyConversion, CurrencyStatistics

currency_list = ['USD', 'EUR', 'RUB', 'UAH', 'CNY']

currency_values = {'USD': 0, 'EUR': 0, 'RUB': 0, 'UAH': 0, 'CNY': 0}

currency_conversion = [
    ['USD','EUR'],
    ['EUR','USD'],
    ['USD','RUB'],
    ['USD','UAH'],
    ['USD','CNY']
]

LATENCY_DAYS=1
SECONDS_IN_DAY=86400

def update_info():
    checkable_currency = get_object_or_404(Currency, abbreviation='USD')
    last_updated = checkable_currency.last_updated
    from_last_update = (datetime.datetime.now(timezone.utc) - last_updated).total_seconds()
    from_last_update = int(from_last_update / SECONDS_IN_DAY)
    if (from_last_update >= LATENCY_DAYS):
        get_currencies()
        get_statistics_list()
        get_conversions()


def get_statistics_list():
    raw_content = get_raw_statistics_list()
    CurrencyStatistics.objects.filter(rate__isnull=False).delete()
    for content in raw_content[0]:
        currency_statistics = CurrencyStatistics.objects.create()
        currency_statistics.rate = content['Cur_OfficialRate']
        currency_statistics.abbreviation = 'USD'
        currency_statistics.date = 
        currency_statistics.save()

    for content in raw_content[1]:
        currency_statistics = CurrencyStatistics.objects.create()
        currency_statistics.rate = content['Cur_OfficialRate']
        currency_statistics.abbreviation = 'EUR'
        currency_statistics.date = 
        currency_statistics.save()


def get_conversions():
    CurrencyConversion.objects.filter(value__isnull=False).delete()
    for conversion in currency_conversion:
        currency_conversion = CurrencyConversion.objects.create()
        currency_conversion.value = currency_values[conversion[0]] / currency_values[conversion[1]]
        currency_conversion.currency_from = conversion[0]
        currency_conversion.currency_to = conversion[1]
        currency_conversion.save()

def get_currencies():
    raw_content = get_raw_currencies()
    Currency.objects.filter(scaele__isnull=False).delete()
    for content in raw_content:
        currency = Currency.objects.create()
        currency.scale = content['Cur_Scale']
        currency.rate = content['Cur_OfficialRate']
        currency.abbreviation = content['Cur_Abbreviation']
        currency.save()


def get_raw_currencies():
    json_content = []
    for currency_id in currency_list:
        currency = get_currency(currency_id)
        if currency and currency != '':
            value = json.loads(currency)
            json_content.append(value)
            currency_values[value['Cur_Abbreviation']] = value['Cur_OfficialRate']/value['Cur_Scale']

    return json_content

def get_currency(id):
    base_url = 'http://www.nbrb.by/API/'
    query = 'ExRates/Rates/' + id + '?ParamMode=2'
    content = ''
    try:
        content = urllib.request.urlopen(base_url + query).read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print("error during fetching currency")
        print(e)
    return content

def get_raw_statistics_list():
    json_content = []
    id='145'
    json_content.append(get_statistics(id))
    id='292'
    json_content.append(get_statistics(id))
    return json_content


def get_statistics(id):
    to_date = datetime.now()
    delta = timedelta(days=30)
    from_date = to_date - delta
    end_date = to_date.strftime('%d+%b+%Y')
    start_date = from_date.strftime('%d+%b+%Y')

    base_url = 'http://www.nbrb.by/API/'
    query = 'ExRates/Rates/Dynamics/' + id + '?startDate='+ start_date + '&endDate=' + end_date
    json_content = ''
    try:
        content = urllib.request.urlopen(base_url + query).read().decode('utf-8')
        json_content = json.loads(content)
    except urllib.error.HTTPError as e:
        print("error during fetching currency")
        print(e)

    return json_content


import json
import urllib
from datetime import timedelta
from datetime import datetime

currency_list = ['USD', 'EUR', 'RUB', 'UAH', 'CNY']

currency_values = {'USD': 0, 'EUR': 0, 'RUB': 0, 'UAH': 0, 'CNY': 0}

currency_conversion = [
    ['USD','EUR'],
    ['EUR','USD'],
    ['USD','RUB'],
    ['USD','UAH'],
    ['USD','CNY']
]

def get_conversions():
    result = []
    for conversion in currency_conversion:
        value = []
        value.append(conversion[0] + ' / ' + conversion[1])
        value.append(currency_values[conversion[0]] / currency_values[conversion[1]])
        result.append(value)
    return result

def get_currencies():
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

def get_statistics_list():
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


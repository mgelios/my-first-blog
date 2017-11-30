import json
import urllib
from datetime import timedelta
from datetime import datetime

def get_currencies():
    json_content = []

    currency = get_currency('RUB')
    if currency and currency != '':
        json_content.append(json.loads(currency))

    currency = get_currency('USD')
    if currency and currency != '':
        json_content.append(json.loads(currency))

    currency = get_currency('EUR')
    if currency and currency != '':
        json_content.append(json.loads(currency))
        
    currency = get_currency('UAH')
    if currency and currency != '':
        json_content.append(json.loads(currency))

    currency = get_currency('CNY')
    if currency and currency != '':
        json_content.append(json.loads(currency))

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

def get_statistics():
    to_date = datetime.now()
    delta = timedelta(days=30)
    from_date = to_date - delta
    end_date = to_date.strftime('%d+%b+%Y')
    start_date = from_date.strftime('%d+%b+%Y')
    id='145'

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


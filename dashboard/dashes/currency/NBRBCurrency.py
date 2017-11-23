import json
import urllib

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

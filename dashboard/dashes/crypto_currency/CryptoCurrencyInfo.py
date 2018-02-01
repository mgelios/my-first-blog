import json
import urllib

from datetime import timedelta
from datetime import datetime, timezone

from django.shortcuts import get_object_or_404

from dashboard.models import CryptoCurrency, CryptoMarket

API_URL = 'https://api.coinmarketcap.com/v1/'
API_TYPE_TICKER = 'ticker/'
API_TYPE_GLOBAL = 'global/'
LIMIT_SUFFIX = '?limit='
LIMIT_AMOUNT = '10'

SPECIAL_IDS = ['nem', 'stellar', 'zcash', 'siacoin', 'golem-network-tokens', 'pivx', 'expanse']

LATENCY = 300

def update_info():
    test_market = None
    try:
        test_market = CryptoMarket.objects.get()
    except CryptoMarket.DoesNotExist:
        test_market = None

    if (test_market == None):
        update_db()
    else:
        last_updated = test_market.last_updated
        from_last_update = (datetime.now(timezone.utc) - last_updated).total_seconds()
        if (from_last_update >= LATENCY):
            update_db()

def update_db():
    raw_currencies = get_info()
    raw_market = get_market_info()
    CryptoCurrency.objects.filter(name__isnull=False).delete()
    CryptoMarket.objects.filter(total_usd__isnull=False).delete()
    for raw_currency in raw_currencies:
        currency = CryptoCurrency.objects.create()
        currency.name = raw_currency['name']
        currency.symbol = raw_currency['symbol']
        currency.rank = raw_currency['rank']
        currency.price_btc = raw_currency['price_btc']
        currency.price_usd = raw_currency['price_usd']
        currency.change_24h = raw_currency['percent_change_24h']
        currency.save()
    print(raw_market)
    market = CryptoMarket.objects.create()
    market.total_usd = int(raw_market[0]['total_market_cap_usd'])
    market.total_usd_day_volume = int(raw_market[0]['total_24h_volume_usd'])
    market.active_markets = int(raw_market[0]['active_markets'])
    market.active_currencies = int(raw_market[0]['active_currencies'])
    market.bitcoin_percent = float(raw_market[0]['bitcoin_percentage_of_market_cap'])
    market.save()



def get_market_info():
    json_content = []
    try:
        content = urllib.request.urlopen(API_URL + API_TYPE_GLOBAL + LIMIT_SUFFIX + LIMIT_AMOUNT).read().decode('utf-8')
        json_content.append(json.loads(content))
    except urllib.error.HTTPError:
        print('error during fetching crypto currency market info')
    return json_content

#get both top and special currencies
def get_info():
    content = get_currencies()[0]
    special_content = get_special_currencies()
    for special_currency in special_content:
        content.append(special_currency[0])

    content = remove_duplicates(content)
    content.sort(key=get_key)
    return content

#get top currencies
def get_currencies():
    json_content = []
    try:
        content = urllib.request.urlopen(API_URL + API_TYPE_TICKER + LIMIT_SUFFIX + LIMIT_AMOUNT).read().decode('utf-8')
        json_content.append(json.loads(content))
    except urllib.error.HTTPError:
        print("error during fetching crypto currency")
    return json_content

#get special currencies from list
def get_special_currencies():
    json_content = []
    try:
        for special_id in SPECIAL_IDS:
            content = urllib.request.urlopen(API_URL + API_TYPE_TICKER + special_id).read().decode('utf-8')
            json_content.append(json.loads(content))
    except urllib.error.HTTPError:
        print("error during fetching crypto currency")
    return json_content

#get sort key 
def get_key(item):
    return int(item['rank'])

def remove_duplicates(content):
    result = []
    for i in range(len(content)):
        found = False
        for j in range(i):
            if (content[i]['id'] == content[j]['id']):
                found = True
        if (not found):
            result.append(content[i])
    return result


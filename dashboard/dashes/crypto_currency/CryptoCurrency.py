import json
import urllib

API_URL = 'https://api.coinmarketcap.com/v1/ticker/'
LIMIT_SUFFIX = '?limit='
LIMIT_AMOUNT = '10'

SPECIAL_IDS = ['nem', 'stellar', 'zcash', 'siacoin', 'golem-network-tokens', 'pivx', 'expanse']

#get top currencies
def get_currencies():
    json_content = []
    try:
        content = urllib.request.urlopen(API_URL + LIMIT_SUFFIX + LIMIT_AMOUNT).read().decode('utf-8')
        json_content.append(json.loads(content))
    except urllib.error.HTTPError:
        print("error during fetching crypto currency")
    return json_content

#get special currencies from list
def get_special_currencies():
    json_content = []
    try:
        for special_id in SPECIAL_IDS:
            content = urllib.request.urlopen(API_URL + special_id).read().decode('utf-8')
            json_content.append(json.loads(content))
    except urllib.error.HTTPError:
        print("error during fetching crypto currency")
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


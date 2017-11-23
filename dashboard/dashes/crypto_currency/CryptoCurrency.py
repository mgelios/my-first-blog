import json
import urllib

API_URL = 'https://api.coinmarketcap.com/v1/ticker/'
LIMIT_SUFFIX = '?limit='
LIMIT_AMOUNT = '10'

def get_currencies():
    json_content = []
    try:
        content = urllib.request.urlopen(API_URL + LIMIT_SUFFIX + LIMIT_AMOUNT).read().decode('utf-8')
        json_content.append(json.loads(content))
    except urllib.error.HTTPError:
        print("error during fetching crypto currency")
    return json_content

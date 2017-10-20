import json
import urllib

def get_currencies():
    json_content = []

    json_content.append(json.loads(get_currency('298')))
    json_content.append(json.loads(get_currency('292')))
    json_content.append(json.loads(get_currency('145')))
    return json_content

def get_currency(id):
    base_url = 'http://nbrb.by/API/'
    query = 'ExRates/Rates/' + id
    content = ''
    try:
        content = urllib.request.urlopen(base_url + query).read().decode('utf-8')
    except urllib.error.HTTPError:
        print("error during fetching currency")
    return content

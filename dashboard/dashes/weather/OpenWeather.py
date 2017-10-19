import json
import urllib

def forecast():
    json_content = []
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    query = 'q=Minsk,by&appid=0502d0f1f744a28dd8065598094fa1db&units=metric'
    content = urllib.request.urlopen(base_url + query).read().decode('utf-8')
    json_content.append(json.loads(content))
    query = 'q=Kapyl,by&appid=0502d0f1f744a28dd8065598094fa1db&units=metric'
    content = urllib.request.urlopen(base_url + query).read().decode('utf-8')
    json_content.append(json.loads(content))
    return json_content
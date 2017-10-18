import urllib

def forecast():
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    query = 'q=Minsk,by&appid=0502d0f1f744a28dd8065598094fa1db'
    content = urllib.request.urlopen(base_url + query).read()
    return content
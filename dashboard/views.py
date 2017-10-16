from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
import urllib

#Post actions section

def dash_list(request):
    content = weather_forecast()
    return render(request, 'base.html', {'content': content})


def weather_forecast():
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    query = 'q=Minsk,by&appid=0502d0f1f744a28dd8065598094fa1db'
    content = urllib.request.urlopen(base_url + query).read()
    return content
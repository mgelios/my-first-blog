from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from dashboard.dashes.weather import OpenWeather


#Post actions section

def dash_list(request):
    content = OpenWeather.forecast()
    return render(request, 'base.html', {'content': content})



from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
import urllib.request

# Create your views here.
def apps_list(request):
    return render(request, 'landing/main.html')

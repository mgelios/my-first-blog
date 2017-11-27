from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone

from .models import SecretMessage

import urllib.request

# Create your views here.
def apps_list(request):
    return render(request, 'landing/main.html')

@login_required
def secret_message_new(request):
    return render(request, 'landing/main.html')

@login_required
def secret_message_list(request):
    messages = SecretMessage.objects.filter(text__isnull=False).order_by('date')
    return render(request, 'landing/messages.html', {'secret_messages': messages})

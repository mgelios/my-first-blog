from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone

from .models import SecretMessage
from .common_settings import versions

import urllib.request


def show_greeting(request):
    return render(request, 'landing/greeting.html')

def apps_list(request):
    return render(request, 'landing/main.html')

@login_required
def secret_message_new(request):
    return render(request, 'landing/main.html')

@login_required
def secret_message_list(request):
    messages = SecretMessage.objects.filter(text__isnull=False).order_by('date')
    return render(request, 'landing/messages.html', {'secret_messages': messages})

def info_about(request):
    return  render(request, 'about/base.html', {'versions' : versions})

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            new_user = form.save()
            new_user.save()
            return redirect('apps_list')
    return render(request, 'registration/register.html', {'form': form})
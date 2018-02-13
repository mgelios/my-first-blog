from django.shortcuts import render
from django.http import HttpResponse


def telegram_bot(request, bot_token):
    return HttpResponse('<h1>It okayyy</h1>')

from django.shortcuts import render
from django.http import HttpResponse


def telegram_bot(request):
    return HttpResponse('<h1>It okayyy</h1>')

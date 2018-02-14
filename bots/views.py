from django.shortcuts import render
from django.http import HttpResponse

from .apps import TelegramBot

my_telegram_id = '@master_gelios'

def telegram_bot(request, bot_token):
    if TelegramBot.webhook_started:
        bot = TelegramBot.bot
        updater = TelegramBot.updater
        dispatcher = TelegramBot.dispatcher
        try:
            update = telegram.Update.de_json(data, bot)
            dispatcher.process_update(update)
        except TelegramError as er:
            print("Error occured during while handling message")
    return HttpResponse('<h1>It okayyy</h1>')

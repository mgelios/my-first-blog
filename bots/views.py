from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

import telegram

from .apps import TelegramBot

my_telegram_id = '@master_gelios'

@csrf_exempt
def telegram_bot(request, bot_token):
    print('### telegram bot endoint called')
    if TelegramBot.webhook_started:
        bot = TelegramBot.bot
        updater = TelegramBot.updater
        dispatcher = TelegramBot.dispatcher
        try:
            print('### bot, updater, dispatcher recieved')
            update = telegram.Update.de_json(data, bot)
            dispatcher.process_update(update)
        except TelegramError as er:
            print('### ')
    return JsonResponse({})

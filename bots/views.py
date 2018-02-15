from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

import telegram
import json
from telegram.error import InvalidToken, TelegramError, BadRequest

from .apps import TelegramBot


my_telegram_nickname = '@mgelios'
my_telegram_id = 396394358

@csrf_exempt
def test_endpoint(request):
    bot = TelegramBot.bot
    bot.send_message(chat_id=my_telegram_id, text='LOLed')
    return JsonResponse({})

@csrf_exempt
def telegram_bot(request, bot_token):
    if TelegramBot.webhook_started:
        bot = TelegramBot.bot
        updater = TelegramBot.updater
        dispatcher = TelegramBot.dispatcher
        data = {}
        try:
            data = json.loads(request.body.decode("utf-8"))
        except:
            print('### error during fetching json data')

        try:
            update = telegram.Update.de_json(data, bot)
            dispatcher.process_update(update)
        except TelegramError as er:
            print('### error during dispatch')
    return JsonResponse({})

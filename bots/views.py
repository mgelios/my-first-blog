from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

import telegram
import json
from telegram.error import InvalidToken, TelegramError, BadRequest

from .apps import TelegramBot


my_telegram_id = '@master_gelios'

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

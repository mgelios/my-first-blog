from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

import telegram
import logging

from .apps import TelegramBot

my_telegram_id = '@master_gelios'

logger = logging.getLogger(__name__)

@csrf_exempt
def telegram_bot(request, bot_token):
    logger.debug('### telegram bot endoint called')
    if TelegramBot.webhook_started:
        bot = TelegramBot.bot
        updater = TelegramBot.updater
        dispatcher = TelegramBot.dispatcher
        try:
            logger.debug('### bot, updater, dispatcher recieved')
            update = telegram.Update.de_json(data, bot)
            dispatcher.process_update(update)
        except TelegramError as er:
            logger.warn('### ')
    return JsonResponse({})

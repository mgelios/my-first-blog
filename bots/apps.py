from django.apps import AppConfig
from django.conf import settings

import telegram
import logging

from telegram.ext import Updater
from telegram.ext import CommandHandler

from telegram.error import InvalidToken, TelegramError, BadRequest

TELEGRAM_BOT_TOKEN = '460933242:AAEh67xQVBeT37EwN84iudv80tbYBsOY1QA'
TELEGRAM_BOT_SUFFIX = 'bots/telegram/'
TELEGRAM_BOT_WEBHOOK_ADDR = 'https://mgelios.pythonanywhere.com/'

logger = logging.getLogger(__name__)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Im a bot,  bloa blaoa bloa')

class TelegramBot(AppConfig):
    name = 'bots'
    verbose_name = 'Telegram bot'
    updater = None
    bot = None
    dispatcher = None
    webhook_started = False

    def ready(self):
        updater = Updater(token=TELEGRAM_BOT_TOKEN)
        bot = updater.bot
        dispatcher = updater.dispatcher
        start_handler = CommandHandler('start', start)
        dispatcher.add_handler(start_handler)
        if settings.TELEGRAM_BOT_ALLOWED:
            try:
                bot.setWebhook(url=TELEGRAM_BOT_WEBHOOK_ADDR+TELEGRAM_BOT_SUFFIX+TELEGRAM_BOT_TOKEN+'/')
                webhook_started = True
                logger.debug('### webhook successfuly started')
            except BadRequest as er:
                logger.warn('### error occured during setting webhook')


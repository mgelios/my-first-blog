from django.apps import AppConfig
from django.conf import settings

import telegram

from telegram.ext import Updater
from telegram.ext import CommandHandler

from telegram.error import InvalidToken, TelegramError, BadRequest

TELEGRAM_BOT_TOKEN = '460933242:AAEh67xQVBeT37EwN84iudv80tbYBsOY1QA'
TELEGRAM_BOT_SUFFIX = 'bots/telegram/'
TELEGRAM_BOT_WEBHOOK_ADDR = 'https://mgelios.pythonanywhere.com/'

class TelegramBot(AppConfig):
    name = 'bots'
    verbose_name = 'Telegram bot'
    updater = None
    bot = None
    dispatcher = None
    webhook_started = False

    def ready(self):
        import bots.telegram_handlers
        TelegramBot.updater = Updater(token=TELEGRAM_BOT_TOKEN)
        TelegramBot.bot = TelegramBot.updater.bot
        TelegramBot.dispatcher = TelegramBot.updater.dispatcher
        if settings.TELEGRAM_BOT_ALLOWED:
            try:
                telegram_handlers.promote_handlers(TelegramBot.dispatcher)
                TelegramBot.bot.setWebhook(url=TELEGRAM_BOT_WEBHOOK_ADDR+TELEGRAM_BOT_SUFFIX+TELEGRAM_BOT_TOKEN+'/')
                TelegramBot.webhook_started = True
                print('### webhook successfuly started')
            except BadRequest as er:
                print('### error occured during setting webhook')


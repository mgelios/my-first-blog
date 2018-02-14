from django.apps import AppConfig
from django.conf import settings

import telegram

from telegram.ext import Updater
from telegram.ext import CommandHandler

from telegram.error import InvalidToken, TelegramError, BadRequest

TELEGRAM_BOT_TOKEN = '460933242:AAEh67xQVBeT37EwN84iudv80tbYBsOY1QA'
TELEGRAM_BOT_SUFFIX = 'bots/telegram/'
TELEGRAM_BOT_WEBHOOK_ADDR = 'https://mgelios.pythonanywhere.com/'

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Im a bot,  bloa blaoa bloa')

def callback_test(bot, job):
    bot.send_message(chat_id='@master_gelios', text='LOLed')

class TelegramBot(AppConfig):
    name = 'bots'
    verbose_name = 'Telegram bot'
    updater = None
    bot = None
    dispatcher = None
    webhook_started = False

    def ready(self):
        TelegramBot.updater = Updater(token=TELEGRAM_BOT_TOKEN)
        TelegramBot.bot = TelegramBot.updater.bot
        TelegramBot.dispatcher = TelegramBot.updater.dispatcher
        start_handler = CommandHandler('start', start)
        TelegramBot.dispatcher.add_handler(start_handler)
        if settings.TELEGRAM_BOT_ALLOWED:
            try:
                TelegramBot.bot.setWebhook(url=TELEGRAM_BOT_WEBHOOK_ADDR+TELEGRAM_BOT_SUFFIX+TELEGRAM_BOT_TOKEN+'/')
                TelegramBot.webhook_started = True
                TelegramBot.updater.job_queue.run_repeating(callback_test, interval=300, first=0)
                print('### webhook successfuly started')
            except BadRequest as er:
                print('### error occured during setting webhook')


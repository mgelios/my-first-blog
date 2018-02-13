from django.apps import AppConfig
from django.conf import settings

import telegram

from telegram.ext import Updater
from telegram.ext import CommandHandler

from telegram.error import InvalidToken, TelegramError, BadRequest

TELEGRAM_BOT_TOKEN = '460933242:AAEh67xQVBeT37EwN84iudv80tbYBsOY1QA'
TELEGRAM_BOT_WEBHOOK_ADDR = 'https:/mgelios.pythonanywhere.com/bots/telegram'


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Im a bot,  bloa blaoa bloa')

class TelegramAppConfig(AppConfig):
    name = 'bots'
    verbose_name = 'Telegram bot'

    def ready(self):
        updater = Updater(token=TELEGRAM_BOT_TOKEN)
        bot = updater.bot
        dispatcher = updater.dispatcher
        start_handler = CommandHandler('start', start)
        dispatcher.add_handler(start_handler)
        print(TELEGRAM_BOT_WEBHOOK_ADDR+'/'+TELEGRAM_BOT_TOKEN+'/')
        if settings.TELEGRAM_BOT_ALLOWED:
            try:
                #bot.setWebhook(url=TELEGRAM_BOT_WEBHOOK_ADDR+'/'+TELEGRAM_BOT_TOKEN+'/')
                updater.start_polling()
            except BadRequest as er:
                print("### unsuccesful starting of webhook because of badrequest")
                print(str(er))



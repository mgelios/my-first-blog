from django.apps import AppConfig
from django.conf import settings

import telegram

from telegram.ext import Updater
from telegram.ext import CommandHandler

TELEGRAM_BOT_TOKEN = '460933242:AAEh67xQVBeT37EwN84iudv80tbYBsOY1QA'
TELEGRAM_BOT_WEBHOOK_ADDR = 'https:/mgelios.pythonanywhere.com:8443/bots/telegram'


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
        if settings.TELEGRAM_BOT_ALLOWED:
            bot.setWebhook(url=TELEGRAM_BOT_WEBHOOK_ADDR,
                           allowed_updates='ALL')


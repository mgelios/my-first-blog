from telegram.ext import CommandHandler, MessageHandler, Filters
from django_telegrambot.apps import DjangoTelegramBot
from dashboard.dashes.weather import OpenWeather
from dashboard.dashes.currency import NBRBCurrency


import logging

logger = logging.getLogger(__name__)

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')

def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='wow, somebody needs help!')

def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def weather(bot, update):
    forecasts = OpenWeather.forecast()
    final_string = ''
    for forecast in forecasts:
        header_string = 'Погода в городе {0} \n'.format(forecast[0].get('name'))
        temperature_string = 'Температура: {0} \n'.format(forecast[0].get('main').get('temp'))
        humidity_string = 'Влажность: {0} \n'.format(forecast[0].get('main').get('humidity'))
        weathers = forecast[0].get('weather')
        weather_string = ''
        for weather in weathers[:-1]:
            weather_string = weather_string + weather.get("description") + ', '
        weather_string = weather_string + weathers[-1].get("description") + '\n'
        final_string = final_string + header_string + temperature_string + humidity_string + weather_string

    bot.sendMessage(update.message.chat_id, text=final_string)

def currency(bot, update):
    currencies = NBRBCurrency.get_currencies()
    final_string = 'Курсы валют от НБРБ: \n'
    for currency in currencies:
        final_string = final_string + '{0} {1} = {2} BYN \n'.format(currency.get('Cur_Scale'), currency.get('Cur_Abbreviation'), currency.get('Cur_OfficialRate'))
    bot.sendMessage(update.message.chat_id, text=final_string)


def main():
    logger.info("Loading handlers for telegram bot")

    dp = DjangoTelegramBot.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("weather", weather))
    dp.add_handler(CommandHandler("погода", weather))
    dp.add_handler(CommandHandler("currency", currency))
    dp.add_handler(CommandHandler("курсы", currency))

    dp.add_handler(MessageHandler([Filters.text], echo))

    dp.add_error_handler(error)



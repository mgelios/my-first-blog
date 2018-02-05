from telegram.ext import CommandHandler, MessageHandler, Filters, JobQueue
from django_telegrambot.apps import DjangoTelegramBot
from dashboard.dashes.weather import OpenWeather
from dashboard.dashes.currency import NBRBCurrency
from dashboard.dashes.crypto_currency import CryptoCurrencyInfo

from .model import Weather
from .model import Currency
from .model import CryptoCurrency

import logging

logger = logging.getLogger(__name__)

help_message = 'Добро пожаловать в гости к mgbot!\nПо сути - это бот-комбайн\nПоясню. Одной тематикой он не ограничен. Информация, которая здесь может быть получена довольно разнообразна.\n'
help_message_commands = 'На данный момент присутствуют следующие комманды:\nweather - информация о погоде\ncurrency - курсы валют НБРБ\nconversion - конверсия валют\ncrypto - курсы криптовалют'

chat_ids = set()

def get_weather_message():
    OpenWeather.update_info()
    weather = Weather.objects.filter(city_name='Minsk')
    final_string = ''
    header_string = 'Погода в городе {0} \n'.format(weather.city_name)
    temperature_string = 'Температура: {0} \n'.format(weather.temperature)
    humidity_string = 'Влажность: {0} \n'.format(weather.humidity)
    weather_string = weather.description
    final_string = final_string + header_string + temperature_string + humidity_string + weather_string
    return final_string

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')

def help(bot, update):
    bot.sendMessage(update.message.chat_id, text=help_message + help_message_commands)

def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def weather(bot, update):
    bot.sendMessage(update.message.chat_id, text=get_weather_message())

def currency(bot, update):
    NBRBCurrency.update_info()
    currencies = Currency.objects.filter(rate__isnull=False)
    final_string = 'Курсы валют от НБРБ: \n'
    for currency in currencies:
        final_string = final_string + '{0} {1} = {2} BYN \n'.format(currency.scale, currency.abbreviation, currency.rate)
    bot.sendMessage(update.message.chat_id, text=final_string)

def currency_conversions(bot, update):
    NBRBCurrency.update_info()
    conversions = CurrencyConversion.objects.filter(currency_from__isnull=False)
    final_string = 'Конверсия курсов валют от НБРБ\n'
    for conversion in conversions:
        final_string = final_string + conversion.currency_from + ' / ' + conversion.currency_to + ': ' + str(conversion.value) + '\n'
    bot.sendMessage(update.message.chat_id, text=final_string)

def crypto(bot, update):
    CryptoCurrencyInfo.update_info()
    currencies = CryptoCurrency.objects.order_by('rank')
    final_string = 'Курсы криптовалют:\n'
    for currency in currencies:
        final_string = final_string + currency.rank + '. ' + currency.name + ': ' + currency.price_usd + '$\n'
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
    dp.add_handler(CommandHandler("crypto", crypto))
    dp.add_handler(CommandHandler("криптовалюты", crypto))
    dp.add_handler(CommandHandler("conversion", currency_conversions))
    dp.add_handler(CommandHandler("конверсия", currency_conversions))

    dp.add_handler(MessageHandler([Filters.text], echo))

    dp.add_error_handler(error)



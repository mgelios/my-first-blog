from django.db import models
from django.utils import timezone

from dashboard.models import Weather
from dashboard.models import Currency
from dashboard.models import CryptoMarket
from dashboard.models import CryptoCurrency
from dashboard.models import CurrencyConversion
from dashboard.models import CurrencyStatistics

from dashboard.dashes.weather import OpenWeather
from dashboard.dashes.currency import NBRBCurrency
from dashboard.dashes.crypto_currency import CryptoCurrencyInfo


from telegram.ext import CommandHandler, MessageHandler, Filters, JobQueue

help_message = 'Добро пожаловать в гости к mgbot!\nПо сути - это бот-комбайн\nПоясню. Одной тематикой он не ограничен. Информация, которая здесь может быть получена довольно разнообразна.\n'
help_message_commands = 'На данный момент присутствуют следующие комманды:\nweather - информация о погоде\ncurrency - курсы валют НБРБ\nconversion - конверсия валют\ncrypto - курсы криптовалют'

chat_ids = set()



def get_weather_message():
    OpenWeather.update_info()
    weather = Weather.objects.filter(city_name='Minsk')[0]
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
    print('crypto debug info')
    CryptoCurrencyInfo.update_info()
    currencies = CryptoCurrency.objects.order_by('rank')
    final_string = 'Курсы криптовалют:\n'
    for currency in currencies:
        final_string = final_string + str(currency.rank) + '. ' + currency.name + ': ' + str(currency.price_usd) + '$\n'
    bot.sendMessage(update.message.chat_id, text=final_string)

def promote_handlers(dispatcher):
    print('telegrambot init')
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("weather", weather))
    dispatcher.add_handler(CommandHandler("погода", weather))
    dispatcher.add_handler(CommandHandler("currency", currency))
    dispatcher.add_handler(CommandHandler("курсы", currency))
    dispatcher.add_handler(CommandHandler("crypto", crypto))
    dispatcher.add_handler(CommandHandler("криптовалюты", crypto))
    dispatcher.add_handler(CommandHandler("conversion", currency_conversions))
    dispatcher.add_handler(CommandHandler("конверсия", currency_conversions))



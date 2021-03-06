from django.db import models
from django.utils import timezone

from dashboard.models import Weather
from dashboard.models import Currency
from dashboard.models import CryptoMarket
from dashboard.models import CryptoCurrency
from dashboard.models import CurrencyConversion
from dashboard.models import CurrencyStatistics
from dashboard.models import RadiotArticle

from dashboard.dashes.weather import OpenWeather
from dashboard.dashes.currency import NBRBCurrency
from dashboard.dashes.crypto_currency import CryptoCurrencyInfo
from dashboard.dashes.news import Radiot


from telegram.ext import CommandHandler, MessageHandler, Filters, JobQueue

help_message = 'Добро пожаловать в гости к mgbot!\nПо сути - это бот-комбайн\nПоясню. Одной тематикой он не ограничен. Информация, которая здесь может быть получена довольно разнообразна.\n'
help_message_commands = 'На данный момент присутствуют следующие комманды:\nweather - информация о погоде\ncurrency - курсы валют НБРБ\nconversion - конверсия валют\ncrypto - курсы криптовалют'

chat_ids = set()



def news(bot, update):
    final_string = ''
    Radiot.update_info()
    news = RadiotArticle.objects.order_by('-radiot_ts')
    for article in news[0:5:1]:
        final_string = final_string + article.title + '\n'
        final_string = final_string + article.link + '\n\n'
    bot.sendMessage(update.message.chat_id, text=final_string)

def get_weather_message(requested_city='minsk'):
    OpenWeather.update_info(requested_city)
    weather = Weather.objects.filter(requested_city=requested_city)[0]
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

def weather(bot, update, args):
    text = ''
    if (len(args) == 0):
        text = get_weather_message()
    else:
        text = get_weather_message(args[0])
    bot.sendMessage(update.message.chat_id, text=text)

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
    dispatcher.add_handler(CommandHandler("help",help))
    dispatcher.add_handler(CommandHandler(command="weather", callback=weather, pass_args=True))
    dispatcher.add_handler(CommandHandler("погода", weather))
    dispatcher.add_handler(CommandHandler("currency", currency))
    dispatcher.add_handler(CommandHandler("курсы", currency))
    dispatcher.add_handler(CommandHandler("crypto", crypto))
    dispatcher.add_handler(CommandHandler("криптовалюты", crypto))
    dispatcher.add_handler(CommandHandler("conversion", currency_conversions))
    dispatcher.add_handler(CommandHandler("конверсия", currency_conversions))
    dispatcher.add_handler(CommandHandler("news", news))
    dispatcher.add_handler(CommandHandler("новости", news))



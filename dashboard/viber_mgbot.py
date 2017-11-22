from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

bot_configuration = BotConfiguration(
    name='mgbot',
    auth_token='46f8cbe1dee7d22a-2654d549e59d8703-5d9a149e324492c0'
)

viber = Api(bot_configuration)
viber.set_webhook('https://mgelios.pythonanywhere.com/viber/mgbot')

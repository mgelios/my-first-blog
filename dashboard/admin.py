from django.contrib import admin
from .models import Weather, WeatherForecast
from .models import Currency, CurrencyStatistics, CurrencyConversion
from .models import CryptoCurrency, CryptoMarket
from .models import DevByEvent

admin.site.register(Weather)
admin.site.register(WeatherForecast)
admin.site.register(Currency)
admin.site.register(CurrencyConversion)
admin.site.register(CurrencyStatistics)
admin.site.register(CryptoCurrency)
admin.site.register(CryptoMarket)
admin.site.register(DevByEvent)


from django.contrib import admin
from .models import Weather, WeatherForecast, Currency, CurrencyStatistics, CurrencyConversion

admin.site.register(Weather)
admin.site.register(WeatherForecast)
admin.site.register(Currency)
admin.site.register(CurrencyConversion)
admin.site.register(CurrencyStatistics)



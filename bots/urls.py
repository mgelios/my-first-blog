from django.conf.urls import url
from django.urls import path, re_path, include

from . import views
from . import apps

suffix = apps.TELEGRAM_BOT_SUFFIX

urlpatterns = [
    url(r'{}(?P<bot_token>.+?)/$'.format(suffix), views.telegram_bot, name='telegram_bot'),
]
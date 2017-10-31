from dashboard.dashes.telegram_bot.bot_views import StartView

urlpatterns=[
    command('start', StartView.as_command_view()),
]

bothandlers=[
    command('start', StartView.as_command_view()),
]
# Generated by Django 2.0.2 on 2018-02-05 10:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoCurrency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('symbol', models.CharField(default='', max_length=200)),
                ('rank', models.IntegerField(default=0)),
                ('price_usd', models.FloatField(default=0.0)),
                ('price_btc', models.FloatField(default=0.0)),
                ('change_24h', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='CryptoMarket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_usd', models.IntegerField(default=0.0)),
                ('total_usd_day_volume', models.IntegerField(default=0.0)),
                ('active_markets', models.IntegerField(default=0.0)),
                ('active_currencies', models.IntegerField(default=0)),
                ('bitcoin_percent', models.FloatField(default=0.0)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scale', models.FloatField(default=0.0)),
                ('rate', models.FloatField(default=0.0)),
                ('abbreviation', models.CharField(default='', max_length=200)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='CurrencyConversion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(default=0.0)),
                ('currency_from', models.CharField(default='', max_length=200)),
                ('currency_to', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CurrencyStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(default='', max_length=200)),
                ('rate', models.FloatField(default=0.0)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_info', models.CharField(default='', max_length=200)),
                ('description', models.CharField(default='', max_length=200)),
                ('icon_name', models.CharField(default='', max_length=200)),
                ('city_name', models.CharField(default='', max_length=200)),
                ('temperature', models.IntegerField(default=0)),
                ('humidity', models.IntegerField(default=0)),
                ('pressure', models.IntegerField(default=0)),
                ('visibility', models.IntegerField(default=0)),
                ('temperature_min', models.IntegerField(default=0)),
                ('temperature_max', models.IntegerField(default=0)),
                ('wind_speed', models.FloatField(default=0.0)),
                ('wind_deg', models.FloatField(default=0.0)),
                ('sunrise', models.DateTimeField(default=django.utils.timezone.now)),
                ('sunset', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='WeatherForecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField(default=0)),
                ('temperature_min', models.IntegerField(default=0)),
                ('temperature_max', models.IntegerField(default=0)),
                ('pressure', models.IntegerField(default=0)),
                ('humidity', models.IntegerField(default=0)),
                ('main_info', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('icon_name', models.CharField(max_length=200)),
                ('wind_speed', models.FloatField(default=0.0)),
                ('wind_deg', models.FloatField(default=0.0)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]

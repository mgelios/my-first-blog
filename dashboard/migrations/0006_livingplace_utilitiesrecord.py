# Generated by Django 2.0.2 on 2018-04-04 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0005_auto_20180315_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='LivingPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('address', models.TextField(default='')),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UtilitiesRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hot_water', models.IntegerField(default=0)),
                ('cold_water', models.IntegerField(default=0)),
                ('electricity', models.IntegerField(default=0)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.LivingPlace')),
            ],
        ),
    ]

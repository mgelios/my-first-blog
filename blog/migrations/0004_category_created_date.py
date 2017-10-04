# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171003_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=128)),
                ('created_at', models.DateTimeField(verbose_name='created at', auto_now_add=True)),
                ('announce_text', models.TextField(verbose_name='announce', max_length=512, blank=True)),
                ('text', models.TextField(verbose_name='text', max_length=4096)),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
                'ordering': ['-created_at'],
            },
        ),
    ]

# Generated by Django 2.0.2 on 2018-02-22 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20180220_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='text',
            field=models.CharField(default='', max_length=1000),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-01 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_park', '0011_auto_20190501_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]

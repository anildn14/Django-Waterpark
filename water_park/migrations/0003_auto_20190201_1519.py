# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-01 09:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_park', '0002_auto_20190131_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_details',
            name='comment_email_id',
            field=models.CharField(max_length=250, validators=[django.core.validators.EmailValidator()]),
        ),
    ]
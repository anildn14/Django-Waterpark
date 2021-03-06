# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-06 04:39
from __future__ import unicode_literals

from django.db import migrations, models
import water_park.validators


class Migration(migrations.Migration):

    dependencies = [
        ('water_park', '0005_auto_20190205_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image_url',
            field=models.FileField(upload_to=b'', validators=[water_park.validators.validate_image_ext]),
        ),
        migrations.AlterField(
            model_name='park_details',
            name='park_logo',
            field=models.FileField(upload_to=b'', validators=[water_park.validators.validate_image_ext]),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.CharField(default=4, max_length=2, validators=[water_park.validators.validate_integers]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile_number',
            field=models.CharField(max_length=15, unique=True, validators=[water_park.validators.validate_integers]),
        ),
    ]

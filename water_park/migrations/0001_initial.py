# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-28 16:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('age', models.IntegerField(null=True)),
                ('marital_status', models.CharField(max_length=10)),
                ('mobile_number', models.CharField(max_length=15, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_name', models.CharField(max_length=50)),
                ('comment_email_id', models.CharField(max_length=250, unique=True)),
                ('comment_text', models.TextField(max_length=1000)),
                ('comment_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=250)),
                ('image_url', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Park_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('park_name', models.CharField(max_length=250)),
                ('park_address', models.TextField(max_length=1000)),
                ('park_time', models.CharField(max_length=50)),
                ('park_logo', models.FileField(upload_to=b'')),
                ('park_url', models.CharField(max_length=1000)),
                ('park_price', models.CharField(max_length=250)),
                ('park_likes', models.IntegerField(default=0)),
                ('is_fav', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='images',
            name='park',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='water_park.Park_Details'),
        ),
    ]
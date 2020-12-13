# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-12-02 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=100)),
                ('Email_address', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=200)),
                ('room_number', models.CharField(max_length=200)),
                ('subjects_taught', models.CharField(max_length=20000)),
                ('profile_image', models.ImageField(default='static/images/placeholder.jpg', upload_to='static/images')),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 08:59
from __future__ import unicode_literals

import chat.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20161224_0552'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResortDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=200)),
                ('document', models.FileField(upload_to=chat.models.resort_path)),
            ],
        ),
    ]

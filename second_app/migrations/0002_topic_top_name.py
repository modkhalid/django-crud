# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-03-23 02:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='top_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=256, unique=True),
            preserve_default=False,
        ),
    ]

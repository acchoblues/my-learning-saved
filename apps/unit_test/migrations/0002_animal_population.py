# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-08 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='population',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]

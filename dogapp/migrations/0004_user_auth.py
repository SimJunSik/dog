# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-17 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogapp', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='auth',
            field=models.IntegerField(default=1),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-24 00:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogapp', '0008_marker'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marker',
            old_name='name',
            new_name='location_name',
        ),
        migrations.AddField(
            model_name='marker',
            name='dog_name',
            field=models.CharField(default='unknown', max_length=40),
        ),
        migrations.AddField(
            model_name='marker',
            name='img_src',
            field=models.CharField(default='', max_length=400),
        ),
    ]

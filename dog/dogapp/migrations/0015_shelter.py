# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-31 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogapp', '0014_takemarker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60)),
                ('addr', models.CharField(default='', max_length=200)),
                ('num', models.CharField(default='', max_length=60)),
                ('location', models.CharField(default='', max_length=60)),
            ],
        ),
    ]

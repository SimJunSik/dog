# Generated by Django 2.0.1 on 2018-01-20 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogapp', '0026_breed_k_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='breed',
            name='result_cnt',
            field=models.IntegerField(default=0),
        ),
    ]

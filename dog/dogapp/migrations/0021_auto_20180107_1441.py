# Generated by Django 2.0 on 2018-01-07 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogapp', '0020_breed_temp_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='breed',
            name='cat_friendliness',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='breed',
            name='dog_friendliness',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 2.0.1 on 2018-01-25 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogapp', '0031_auto_20180124_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_num', models.IntegerField(default=0)),
                ('cnt', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_num', models.IntegerField(default=0)),
                ('cnt', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_num', models.IntegerField(default=0)),
                ('cnt', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_num', models.IntegerField(default=0)),
                ('cnt', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_num', models.IntegerField(default=0)),
                ('cnt', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_num', models.IntegerField(default=0)),
                ('cnt', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_num', models.IntegerField(default=0)),
                ('cnt', models.IntegerField(default=0)),
            ],
        ),
    ]
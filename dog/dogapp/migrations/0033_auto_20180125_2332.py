# Generated by Django 2.0.1 on 2018-01-25 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogapp', '0032_question1_question2_question3_question4_question5_question6_question7'),
    ]

    operations = [
        migrations.AddField(
            model_name='question1',
            name='answer_txt',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='question2',
            name='answer_txt',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='question3',
            name='answer_txt',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='question4',
            name='answer_txt',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='question5',
            name='answer_txt',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='question6',
            name='answer_txt',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='question7',
            name='answer_txt',
            field=models.CharField(default='', max_length=40),
        ),
    ]

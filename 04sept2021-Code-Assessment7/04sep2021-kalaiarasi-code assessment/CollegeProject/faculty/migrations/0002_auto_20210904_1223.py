# Generated by Django 3.2.6 on 2021-09-04 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='password',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AddField(
            model_name='faculty',
            name='username',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
    ]

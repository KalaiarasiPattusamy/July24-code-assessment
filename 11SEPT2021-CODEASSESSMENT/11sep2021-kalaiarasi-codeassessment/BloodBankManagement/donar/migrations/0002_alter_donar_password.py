# Generated by Django 3.2.6 on 2021-09-11 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donar',
            name='password',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 3.2.6 on 2021-09-11 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('bloodgroup', models.CharField(max_length=50)),
                ('mobnum', models.BigIntegerField()),
                ('username', models.CharField(max_length=50)),
                ('password', models.IntegerField(max_length=50)),
            ],
        ),
    ]

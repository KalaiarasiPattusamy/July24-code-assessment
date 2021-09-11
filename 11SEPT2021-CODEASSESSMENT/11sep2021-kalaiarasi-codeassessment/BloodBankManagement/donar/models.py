from django.db import models

# Create your models here.
class Donar(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    bloodgroup=models.CharField(max_length=50)
    mobnum=models.BigIntegerField()
    username=models.CharField(max_length=50)
    password=models.IntegerField()
    
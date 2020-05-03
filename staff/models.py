from django.db import models

# Create your models here.

class Staff(models.Model):
    name=models.CharField(max_length=80)
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    contract=models.CharField(max_length=50)
    qualification=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
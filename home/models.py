from django.db import models
from phone_field import PhoneField
# Create your models here.

class Profile(models.Model):
    age = models.IntegerField()
    address = models.CharField( max_length=200)
    phoneNumber = PhoneField()
    dateOfBirth=models.CharField(max_length=200)
    reminderDate=models.CharField(max_length=200)
    patientId = models.CharField(max_length=20, unique=True)
from django.db import models

# Create your models here.

class Report(models.Model):
    reportDate=models.DateField()
    details=models.CharField( max_length=5000)
    patientId=models.CharField(max_length=20, unique=True)
    appointmentId=models.CharField(max_length=20, unique=True)
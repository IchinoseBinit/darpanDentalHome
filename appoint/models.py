from django.db import models

# Create your models here.

class Appoint(models.Model):
    treatment = models.CharField(max_length=100)
    appointmentDate = models.CharField( max_length=500)
    patientId = models.CharField(max_length=20)


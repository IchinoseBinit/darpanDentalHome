from django.db import models

# Create your models here.

class Feedback(models.Model):
    feedback = models.CharField(max_length=500)
    feedbackDate=models.DateTimeField(auto_now_add=True)
    patientId=models.CharField(max_length=20, unique=True)
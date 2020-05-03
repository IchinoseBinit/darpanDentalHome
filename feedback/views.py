from django.shortcuts import render,redirect
from feedback.models import Feedback

# Create your views here.

def feedback(request):
    feedbackMessage = request.POST['feedback']
    feedback = Feedback.objects.create(feedback=feedbackMessage, patientId=request.user.id)
    return redirect('/home')

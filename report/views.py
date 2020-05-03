from django.shortcuts import render,redirect
from django.contrib import messages
from report.models import Report
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
# Create your views here.


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def report(request):
    if Report.objects.filter(patientId=request.user.id).exists:
        reports=Report.objects.filter(patientId=request.user.id)
        return render(request, 'report.html',{'reports':reports})
    else:
        messages.info(request, "Sorry you dont have any reports yet.")
        return render(request, 'report.html')
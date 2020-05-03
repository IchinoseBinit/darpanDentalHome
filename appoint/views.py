from django.shortcuts import render, redirect
from appoint.models import Appoint
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
# Create your views here.


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def makeAppoint(request):
    if request.method == 'GET':
        return render(request, 'makeAppoint.html')
    else:
        treatment=request.POST['treatment']
        date=request.POST['appointmentDate']
        appoint = Appoint.objects.create(treatment=treatment, appointmentDate=date, patientId=request.user.id)
        return redirect('/home')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def updateAppoint(request):
    if request.method == 'GET':
        return render(request, 'updateAppoint.html')
    else:
        id=request.POST['appointmentId']
        treatment=request.POST['treatment']
        date=request.POST['appointmentDate']
        if Appoint.objects.filter(patientId=request.user.id).exists():
            if Appoint.objects.filter(appointmentId=id).exists:
                Appoint.appointmentDate=date
                Appoint.treatment=treatment
                return redirect('/home')
            else:
                messages.info(request,"Wrong Appointment Id")
                return render(request, 'updateAppointment.html')
        else:
            messages.info(request,"You dont have any appointment")
            return render(request, 'updateAppointment.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)        
@login_required(login_url='/login')
def viewAppoint(request):
    if Appoint.objects.filter(patientId=request.user.id).exists():
        appointments = Appoint.objects.filter(patientId=request.user.id)
        return render(request, 'viewAppoint.html', {'apps':appointments})
    else:
        messages.info(request,"You dont have any appointment")
        return render(request, 'viewAppoint.html')
    

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def cancelAppoint(request):
    if request.method == 'GET':
        return render(request, 'cancelAppoint.html')
    else:
        id=request.POST['appointmentId']
        if Appoint.objects.filter(patientId=request.user.id).exists():
            if Appoint.objects.filter(id=id).exists:
                Appoint.objects.filter(id=id).delete()
                return redirect('/home')
            else:
                messages.info(request,"Wrong Appointment Id")
                return render(request, 'cancelAppointment.html')
        else:
            messages.info(request,"You dont have any appointment")
            return render(request, 'cancelAppointment.html')
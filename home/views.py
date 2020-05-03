from django.shortcuts import render, redirect
from django.contrib import messages, auth
from home.models import Profile
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


# Create your views here.


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def home(request):
    return render(request, 'home.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def profile(request):
    if request.method == "GET":
        if Profile.objects.filter(patientId=request.user.id).exists():
            patient=Profile.objects.filter(patientId=request.user.id).get()
            return render(request, 'profile.html',{'patient':patient})
        else:
            messages.info(request,"Please Update your Profile")
            return render(request, 'profile.html')
    else:
        age=request.POST['age']
        address=request.POST['address']
        phoneNumber=request.POST['phone']
        dateOfBirth=request.POST['dob']
        reminderDate=request.POST['reminder']
        if Profile.objects.filter(patientId=request.user.id).exists():
            newPatient=Profile.objects.filter(patientId=request.user.id)
            newPatient.age=age
            newPatient.address=address
            newPatient.phoneNumber=phoneNumber
            newPatient.dateOfBirth=dateOfBirth
            newPatient.reminderDate=reminderDate
            return render(request, 'profile.html')
        else:
            Profile.objects.create(age=age, address=address, phoneNumber=phoneNumber, dateOfBirth=dateOfBirth, reminderDate=reminderDate, patientId=request.user.id)
            return render(request, 'profile.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    return redirect('/')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def esewa(request):
    if request.method == "GET":
        return render(request, 'esewa.html')
    else:
        return redirect('/home')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def card(request):
    if request.method == "GET":
        return render(request, 'card.html')
    else:
        return redirect('/home')
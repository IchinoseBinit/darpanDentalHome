from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
        
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        myUser = User.objects.all()
        for user in myUser:
            if user is not None:
                auth.login(request, user)
                return redirect('/home')
            else:
                messages.info(request, "Invalid Credentials")
                return render(request, 'login.html')

        

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        username = request.POST['userName'] 
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return render(request, 'register.html')
            else:
                dest = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                dest.save()
                return redirect('/')
        else:
            messages.info(request,"Password unmatched")
            return render(request, 'register.html')

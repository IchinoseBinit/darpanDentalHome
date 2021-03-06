from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register', views.register, name="register"),
    path('home/', include('home.urls')),
]
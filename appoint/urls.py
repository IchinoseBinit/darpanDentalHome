from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('makeAppointment', views.makeAppoint, name="makeAppointment"),
    path('updateAppointment', views.updateAppoint, name="updateAppointment"),
    path('viewAppointment', views.viewAppoint, name="viewAppointment"),
    path('cancelAppointment', views.cancelAppoint, name="cancelAppointment"),
]
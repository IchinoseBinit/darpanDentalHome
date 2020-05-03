from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('profile', views.profile, name="profile"),
    path('logout', views.logout, name="logoutProfile"),
    path('appoint/', include('appoint.urls')),
    path('feedback/', include('feedback.urls')),
    path('report/', include('report.urls')),
    path('pay/esewa', views.esewa, name="esewa"),
    path('pay/card', views.card, name="card")
]
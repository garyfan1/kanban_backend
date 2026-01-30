from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.health_check, name='ping'),
    path('jwt-ping/', views.health_check_jwt, name='jwt-ping'),
]
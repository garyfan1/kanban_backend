from django.urls import path
from rest_framework import routers
from . import views
from .views import TaskViewSet

router = routers.SimpleRouter()
router.register("tasks", TaskViewSet)

urlpatterns = [
    path('ping/', views.health_check, name='ping'),
    path('jwt-ping/', views.health_check_jwt, name='jwt-ping'),
    path("register/", views.RegisterView.as_view(), name="register")
]

urlpatterns += router.urls
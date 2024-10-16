from django.urls import path
from . import views

urlpatterns = [
    path('log/', views.log_water_intake, name='log_water_intake'),
    path('progress/', views.progress, name='progress'),
]

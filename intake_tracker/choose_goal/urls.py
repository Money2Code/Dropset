from django.urls import path
from . import views

urlpatterns = [
     # Add this line to include the logout URL
    path('goals/', views.goals, name='goals'),
]
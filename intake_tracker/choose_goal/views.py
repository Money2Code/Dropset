from django.shortcuts import render
from django.shortcuts import render, redirect
# from .models import CaloriesIntake
# from .forms import CalorieIntakeForm
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def goals(request):
    return render(request,'goals.html')

from django.shortcuts import render, redirect
from .models import WaterIntake
from .forms import WaterIntakeForm
from django.utils import timezone

def log_water_intake(request):
    today = timezone.now().date()
    water_intake, created = WaterIntake.objects.get_or_create(date=today)
   

    print(water_intake, created ,water_intake.goal)
    
    if request.method == "POST":
        form = WaterIntakeForm(request.POST, instance=water_intake)
        if form.is_valid():  # Ensure form validation
            form.save()
            return redirect('progress')
        else:
            print(form.errors)  # Print errors if form is invalid (for debugging)
    else:
        form = WaterIntakeForm(instance=water_intake)

    return render(request, 'log_water_intake.html', {'form': form})


def progress(request):
    today = timezone.now().date()
    print(today)
    water_intake = WaterIntake.objects.filter(date=today).first()
    
    if water_intake:
        percentage = (water_intake.intake / water_intake.goal) * 100
    else:
        percentage = 0

    return render(request, 'progress.html', {'percentage': percentage, 'water_intake': water_intake})

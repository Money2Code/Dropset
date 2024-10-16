from django.shortcuts import render
from .models import Intake

def intake_view(request):
    # Get the latest intake entry or None if it doesn't exist
    intake = Intake.objects.last()

    if intake is None:
        # Default values if no record exists
        # water_intake = 0.0
        # calorie_intake = 0.0
        # water_goal = 2.0  # Default goal in liters
        # calorie_goal = 2000  # Default goal in kcal
        water_intake = 1  # In liters
        calorie_intake = 1200  # In kcal
        water_goal = 5.0
        calorie_goal = 2000
        water_percentage = 0  # No intake, so 0% progress
        calorie_percentage = 0
    else:
        # Use the actual values from the latest Intake entry
        water_intake = intake.water_intake
        calorie_intake = intake.calories_intake
        water_goal = intake.water_goal
        calorie_goal = intake.calorie_goal

        # Calculate percentages
        water_percentage = (water_intake / water_goal) * 100
        calorie_percentage = (calorie_intake / calorie_goal) * 100

    context = {
        'water_intake': water_intake,
        'calorie_intake': calorie_intake,
        'water_goal': water_goal,
        'calorie_goal': calorie_goal,
        'water_percentage': water_percentage,
        'calorie_percentage': calorie_percentage,
    }

    return render(request, 'intake.html', context)



# Create your models here.
from django.db import models

class Intake(models.Model):
    date = models.DateField(auto_now_add=True)
    water_intake = models.FloatField(default=0)  # in liters
    calorie_intake = models.FloatField(default=0)  # in kcal
    water_goal = models.FloatField(default=2.0)  # 2L as the default goal
    calorie_goal = models.IntegerField(default=2000)  # 2000 kcal as the default goal

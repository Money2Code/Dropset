from django.db import models
from django.utils import timezone

class WaterIntake(models.Model):
    date = models.DateField(default=timezone.now)
    intake = models.FloatField(default=0.0)  # Default to 0 liters
    goal=models.FloatField(default=2.0)
 # Daily water intake goal, default 2 liters
    
    

    def __str__(self):
        print(self.date,self.intake,self.goal)
        return f"{self.intake} L on {self.date} at {self.goal}"
    
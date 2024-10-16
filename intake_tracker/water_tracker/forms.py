from django import forms
from .models import WaterIntake

class WaterIntakeForm(forms.ModelForm):
    class Meta:
        model = WaterIntake
        fields = ['intake','goal'] 

    def clean_intake(self):
        intake = self.cleaned_data.get('intake')
        goal = self.cleaned_data.get('goal')
        if intake is None or intake <= 0:
            raise forms.ValidationError("Please enter a valid amount of water intake.")
        return intake 

from django import forms
from .models import CaloriesIntake
from .models import DietPlan


class CalorieIntakeForm(forms.ModelForm):
    class Meta:
        model = CaloriesIntake
        fields = ['protein','carbs','fats','fibers','protein_goal','carbs_goal','fats_goal','fibers_goal'] 


    def clean_intake(self):
        protein = self.cleaned_data.get('protein')
        carbs = self.cleaned_data.get('carbs')
        fats = self.cleaned_data.get('fats')
        fibers = self.cleaned_data.get('fibers')
        protein_goal = self.cleaned_data.get('protein_goal')
        carbs_goal = self.cleaned_data.get('carbs_goal')
        fats_goal = self.cleaned_data.get('fats_goal')
        fibers_goal = self.cleaned_data.get('fibers_goal')

        if protein is None or protein <= 0:
            raise forms.ValidationError("Please enter a valid amount of protein intake.")
        if carbs is None or carbs <= 0:
            raise forms.ValidationError("Please enter a valid amount of carbs intake.")
        if fats is None or fats <= 0:
            raise forms.ValidationError("Please enter a valid amount of fats intake.")
        if fibers is None or fibers <= 0:
            raise forms.ValidationError("Please enter a valid amount of fibers intake.")
        return protein ,carbs ,fats ,fibers ,protein_goal,carbs_goal,fats_goal,fibers_goal
    


class DietPlanForm(forms.ModelForm):
    class Meta:
        model = DietPlan
        fields = ['weight', 'height', 'age', 'gender', 'activity_level']
        widgets = {
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'id': 'weight'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'id': 'height'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'id': 'age'}),
            'gender': forms.Select(attrs={'class': 'form-select', 'id': 'gender'}),
            'activity_level': forms.Select(attrs={'class': 'form-select', 'id': 'activity'}),
        }


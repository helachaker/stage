from django import forms
from .models import Employee, Performance, SatisfactionSurvey, Feedback, Behavior


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'  # Inclut tous les champs du modèle


class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = ['employee', 'evaluation_date', 'performance_rating', 'goals', 'development_plan', 'performance_score', 'promotion', 'salary_increase']


class SatisfactionSurveyForm(forms.ModelForm):
    class Meta:
        model = SatisfactionSurvey
        fields = ['employee', 'survey_date', 'feedback', 'satisfaction_score']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['employee', 'feedback_date', 'feedback_text']

class BehaviorForm(forms.ModelForm):
    class Meta:
        model = Behavior
        fields = ['employee', 'date', 'absenteeism_days', 'overtime_hours', 'training_engagement', 'notes']

from django import forms

class PredictionForm(forms.Form):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    DEPARTMENT_CHOICES = [
        ('HR', 'HR'),
        ('Finance', 'Finance'),
        ('IT', 'IT'),
        ('Sales', 'Sales'),
        # Ajoutez d'autres départements ici
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    position = forms.CharField(max_length=100)
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    age = forms.IntegerField()
    salary = forms.DecimalField(max_digits=10, decimal_places=2)
    performance_rating = forms.DecimalField(max_digits=3, decimal_places=1)
    salary_increase = forms.DecimalField(max_digits=10, decimal_places=2)
    absenteeism_days = forms.IntegerField()
    overtime_hours = forms.IntegerField()
    satisfaction_score = forms.IntegerField()
    feedback_text = forms.CharField(widget=forms.Textarea)

# gestion/forms.py

from django import forms
from .models import ActionPlan

class ActionPlanForm(forms.ModelForm):
    class Meta:
        model = ActionPlan
        fields = ['employee', 'plan', 'details', 'status', 'feedback']  # Utilisez les champs définis dans le modèle

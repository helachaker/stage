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

class PredictForm(forms.Form):
    employee_id = forms.IntegerField(label='Employee ID')
    age = forms.FloatField(label='Age')
    years_at_company = forms.FloatField(label='Years at Company')
    department = forms.ChoiceField(choices=[('HR', 'HR'), ('Finance', 'Finance'), ('Engineering', 'Engineering'), ('Marketing', 'Marketing'), ('Sales', 'Sales')], label='Department')
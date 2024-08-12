from django.shortcuts import redirect, render
from .forms import EmployeeForm, PerformanceForm, SatisfactionSurveyForm, FeedbackForm, BehaviorForm
from .models import Employee, Performance, SatisfactionSurvey, Feedback


def home(request):
    return render(request, 'home.html')

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


def add_performance(request):
    if request.method == "POST":
        form = PerformanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('performance_list')
    else:
        form = PerformanceForm()
    return render(request, 'gestion/add_performance.html', {'form': form})

def performance_list(request):
    performances = Performance.objects.all()
    return render(request, 'gestion/performance_list.html', {'performances': performances})


def add_satisfaction_survey(request):
    if request.method == 'POST':
        form = SatisfactionSurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirection après la soumission
    else:
        form = SatisfactionSurveyForm()
    return render(request, 'gestion/add_satisfaction_survey.html', {'form': form})

def add_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirection après la soumission
    else:
        form = FeedbackForm()
    return render(request, 'gestion/add_feedback.html', {'form': form})

def view_surveys(request):
    surveys = SatisfactionSurvey.objects.all()
    return render(request, 'gestion/view_surveys.html', {'surveys': surveys})

def view_feedbacks(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'gestion/view_feedbacks.html', {'feedbacks': feedbacks})



def success_view(request):
    return render(request, 'gestion/success.html')


def add_behavior(request):
    if request.method == 'POST':
        form = BehaviorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Assurez-vous que vous avez une URL nommée 'success'
    else:
        form = BehaviorForm()
    return render(request, 'gestion/add_behavior.html', {'form': form})

from django.shortcuts import render
import pandas as pd
import joblib
from django.conf import settings

def predict_employee_retention(request):
    # Charger le modèle
    model_path = settings.BASE_DIR / 'projet_rh/model.pkl'
    model = joblib.load(model_path)
    
    if request.method == 'POST':
        # Extraire les données de l'employé depuis le formulaire
        data = {
            'age': int(request.POST['age']),
            'salary': float(request.POST['salary']),
            'performance_rating': float(request.POST['performance_rating']),
            'absenteeism_days': int(request.POST['absenteeism_days']),
            'overtime_hours': int(request.POST['overtime_hours']),
            'satisfaction_score': float(request.POST['satisfaction_score']),
            
        
        }
        
        # Convertir les données en DataFrame
        df = pd.DataFrame([data])
        
        # Faire des prédictions
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0][1]
        
        # Traduire la prédiction en texte
        if prediction == 1:
            result = "L'employé est susceptible de quitter l'entreprise."
        else:
            result = "L'employé n'est pas susceptible de quitter l'entreprise."
        
        context = {
            'result': result,
            'probability': probability * 100
        }
        
        return render(request, 'gestion/predict_result.html', context)
    
    return render(request, 'gestion/predict_form.html')
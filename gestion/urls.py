from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_employee, name='add_employee'),
    path('list/', views.employee_list, name='employee_list'),
    path('add_performance/', views.add_performance, name='add_performance'),
    path('performance_list/', views.performance_list, name='performance_list'),
    path('add_satisfaction_survey/', views.add_satisfaction_survey, name='add_satisfaction_survey'),
    path('add_feedback/', views.add_feedback, name='add_feedback'),
    path('view_surveys/', views.view_surveys, name='view_surveys'),
    path('view_feedbacks/', views.view_feedbacks, name='view_feedbacks'),
    path('success/', views.success_view, name='success'),
    path('add_behavior/', views.add_behavior, name='add_behavior'),
    path('predict/', views.predict_employee_retention, name='predict_employee_retention'),
    path('predict/result/', views.predict_employee_retention, name='predict_result'),  # Route pour les résultats
    path('dashboard/', views.retention_dashboard, name='retention_dashboard'),

]
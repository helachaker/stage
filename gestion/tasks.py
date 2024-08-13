import os
import django
import pandas as pd
from django.core.mail import send_mail
from django.conf import settings
import sys


# Ajouter le répertoire parent de 'projet_rh' à PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projet_rh.settings')
django.setup()

from gestion.models import Employee, SatisfactionSurvey, Performance

def send_turnover_alerts():
    employees = pd.DataFrame(list(Employee.objects.all().values()))
    surveys = pd.DataFrame(list(SatisfactionSurvey.objects.all().values()))
    performances = pd.DataFrame(list(Performance.objects.all().values()))

    df = employees.merge(surveys, on='employee_id', how='left')
    df = df.merge(performances, on='employee_id', how='left')

    df['risk_level'] = df.apply(lambda row: 'High' if row['satisfaction_score'] < 50 and row['performance_score'] < 50 else 'Low', axis=1)
    high_risk_employees = df[df['risk_level'] == 'High']

    for _, employee in high_risk_employees.iterrows():
        send_mail(
            subject=f"Alerte de turnover : {employee['first_name']} à risque élevé de départ",
            message=f"Le modèle prédictif a détecté que {employee['first_name']} ({employee['position']}) présente un risque élevé de départ.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[employee['manager_email']],
        )
        print(f"Alerte envoyée pour {employee['first_name']}")

if __name__ == "__main__":
    send_turnover_alerts()

from celery import shared_task

@shared_task
def send_turnover_alerts_task():
    send_turnover_alerts()

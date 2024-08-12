import pandas as pd
import os
import django
import sys
# Ajouter le répertoire parent à PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configurer les paramètres Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projet_rh.settings')
django.setup()

from gestion.models import Employee, SatisfactionSurvey, Performance
def assess_risk():
    # Récupérer les données des employés
    employees = pd.DataFrame(list(Employee.objects.all().values()))
    surveys = pd.DataFrame(list(SatisfactionSurvey.objects.all().values()))
    performances = pd.DataFrame(list(Performance.objects.all().values()))

    # Joindre les données pour avoir une vue d'ensemble
    df = employees.merge(surveys, on='employee_id', how='left')
    df = df.merge(performances, on='employee_id', how='left')

    # Calculer le risque basé sur certains critères
    df['risk_level'] = df.apply(lambda row: 'High' if row['satisfaction_score'] < 50 and row['performance_score'] < 50 else 'Low', axis=1)

    # Sélectionner les employés à risque élevé
    high_risk_employees = df[df['risk_level'] == 'High']

    return high_risk_employees
 

if __name__ == "__main__":
    assess_risk()
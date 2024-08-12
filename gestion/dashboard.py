import plotly.express as px
import pandas as pd
from .models import SatisfactionSurvey

def generate_retention_dashboard():
    # Récupérer les données de la base de données
    df = pd.DataFrame(list(SatisfactionSurvey.objects.all().values()))

    # Vérifier que les données ne sont pas vides
    if df.empty:
        return None, None

    # Vérifier que la colonne 'satisfaction_score' existe dans le DataFrame
    if 'satisfaction_score' not in df.columns:
        raise ValueError("La colonne 'satisfaction_score' est manquante dans les données")

    # Créer le graphique pour la distribution des scores de satisfaction
    fig_satisfaction = px.histogram(df, x='satisfaction_score', title='Distribution des scores de satisfaction des employés')

    # Vous pouvez ajouter d'autres graphiques ici

    return fig_satisfaction.to_html(full_html=False), None

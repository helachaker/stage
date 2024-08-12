# projet_rh/risk_classification.py

def classify_risk(probability):
    """
    Classifie le risque en fonction de la probabilité prédite.

    Args:
        probability (float): Probabilité que l'employé quitte l'entreprise.

    Returns:
        str: Niveau de risque ('Low Risk', 'Medium Risk', 'High Risk').
    """
    if probability < 0.3:
        return 'Low Risk'
    elif probability < 0.7:
        return 'Medium Risk'
    else:
        return 'High Risk'

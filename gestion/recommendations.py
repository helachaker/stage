def generate_recommendations(employees):
    recommendations = []

    for _, employee in employees.iterrows():
        recommendation = {
            'employee_id': employee['employee_id'],
            'recommendation': ''
        }

        # Exemple de recommandations
        if employee['satisfaction_score'] < 50:
            recommendation['recommendation'] += 'Offrir une formation sur la gestion du stress. '
        if employee['performance_score'] < 50:
            recommendation['recommendation'] += 'Organiser des sessions de coaching avec un mentor. '

        recommendations.append(recommendation)

    return recommendations

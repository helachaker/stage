import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_simulated_data(original_df, num_new_samples):
    np.random.seed(42)

    # Copier les données existantes
    df_new = original_df.copy()

    # Générer de nouvelles données
    for _ in range(num_new_samples):
        new_row = {
            'first_name': np.random.choice(['John', 'Jane', 'Alex', 'Emily']),
            'last_name': np.random.choice(['Doe', 'Smith', 'Johnson', 'Williams']),
            'date_of_birth': (datetime.now() - timedelta(days=np.random.randint(18*365, 60*365))).date(),
            'gender': np.random.choice([0, 1]),  # 0 pour Male, 1 pour Female
            'position': np.random.choice(['Developer', 'Manager', 'Analyst']),
            'department': np.random.choice(['IT', 'HR', 'Finance']),
            'hire_date': (datetime.now() - timedelta(days=np.random.randint(0, 5*365))).date(),
            'salary': np.random.uniform(30000, 120000),
            'performance_rating': np.random.uniform(1, 10),
            'salary_increase': np.random.uniform(0, 0.2),
            'absenteeism_days': np.random.randint(0, 30),
            'overtime_hours': np.random.randint(0, 20),
            'satisfaction_score': np.random.uniform(1, 10),
            'feedback_text': np.random.choice(['Good', 'Average', 'Poor']),
            'will_leave': np.random.choice([0, 1])
        }
        df_new = pd.concat([df_new, pd.DataFrame([new_row])], ignore_index=True)

    return df_new

# Lire le fichier CSV existant
df_original = pd.read_csv('preprocessed_data.csv')

# Générer de nouvelles données
df_extended = generate_simulated_data(df_original, num_new_samples=1000)

# Sauvegarder les données étendues dans un nouveau fichier CSV
df_extended.to_csv('extended_data.csv', index=False)

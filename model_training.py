import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.model_selection import GridSearchCV
import joblib
def preprocess_data(df):
    # Convertir les colonnes de dates en datetime
    df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], errors='coerce')
    df['hire_date'] = pd.to_datetime(df['hire_date'], errors='coerce')

    # Supprimer les lignes avec des valeurs manquantes dans 'date_of_birth'
    df = df.dropna(subset=['date_of_birth'])

    # Calculer l'âge en années
    today = datetime.now().date()
    df['age'] = df['date_of_birth'].apply(lambda x: (today - x.date()).days // 365)

    # Supprimer les colonnes non nécessaires
    df = df.drop(columns=['first_name', 'last_name','date_of_birth', 'hire_date'])

    # Convertir les colonnes de texte en variables catégorielles
    categorical_features = ['gender', 'position', 'department', 'feedback_text']
    df[categorical_features] = df[categorical_features].astype('category')

    # Séparer les caractéristiques (features) et la cible (target)
    X = df.drop(columns=['will_leave'])
    y = df['will_leave']

    return X, y

def build_pipeline():
    # Définir les transformations pour les variables catégorielles
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), ['gender', 'position', 'department', 'feedback_text']),
            ('num', StandardScaler(), ['age', 'salary', 'performance_rating', 'salary_increase', 'absenteeism_days', 'overtime_hours', 'satisfaction_score'])
        ],
        remainder='passthrough'
    )

    # Créer un pipeline avec prétraitement et modèle
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression(max_iter=2000))
    ])

    return pipeline

def train_model(file_path):
    # Lire les données
    df = pd.read_csv(file_path)
    
    # Prétraitement des données
    X, y = preprocess_data(df)
    
    # Vérifier et traiter les valeurs manquantes dans 'will_leave'
    if y.isnull().any():
        print("Des valeurs manquantes ont été trouvées dans 'will_leave'. Les lignes seront supprimées.")
        non_null_indices = y.dropna().index
        X = X.loc[non_null_indices]
        y = y.dropna()
    
    # Construire le pipeline
    pipeline = build_pipeline()

    # Définir la grille de paramètres pour la recherche
    param_grid = {
        'classifier__C': [0.1, 1, 10],
        'classifier__solver': ['lbfgs', 'liblinear']
    }

    # Créer une recherche en grille
    grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X, y)
    
    # Afficher les meilleurs paramètres et score
    print(f"Meilleurs paramètres : {grid_search.best_params_}")
    print(f"Meilleur score : {grid_search.best_score_}")

    # Évaluer le modèle avec les meilleurs paramètres
    best_model = grid_search.best_estimator_
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    best_model.fit(X_train, y_train)
    y_pred = best_model.predict(X_test)
    print(classification_report(y_test, y_pred))
    

   # Sauvegarder le modèle dans un fichier .pkl
    model_save_path = 'model.pkl'
    joblib.dump(best_model, model_save_path)
    print(f"Modèle sauvegardé à l'emplacement : {model_save_path}")

    
    return best_model

# Exécution du code
if __name__ == "__main__":
    model = train_model('extended_data.csv')

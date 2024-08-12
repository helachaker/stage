import pandas as pd

def preprocess_data(csv_file):
    df = pd.read_csv(csv_file)

    # Exemple de prétraitement
    df.fillna(0, inplace=True)  # Remplacer les valeurs manquantes par 0
    df['gender'] = df['gender'].replace({'Male': 0, 'Female': 1, 'Other': 2})  # Encodage des genres
    # Autres prétraitements selon les besoins...

    return df

if __name__ == "__main__":
    csv_file = 'exported_data.csv'
    df = preprocess_data(csv_file)
    df.to_csv('preprocessed_data.csv', index=False)
    print('Prétraitement terminé. Données sauvegardées dans preprocessed_data.csv')

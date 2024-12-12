import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# URL de la page FBref
url = "https://fbref.com/en/squads/b8fd03ef/2023-2024/matchlogs/c9/schedule/Manchester-City-Scores-and-Fixtures-Premier-League"

# Récupération de la page HTML
response = requests.get(url)
if response.status_code != 200:
    print(f"Erreur lors du téléchargement des données. Code: {response.status_code}")
    exit()

# Parser le HTML avec BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Identifier le tableau des matchs
table = soup.find('table', {'id': 'matchlogs_for'})  # L'ID spécifique du tableau

# Extraction des données du tableau
headers = [th.text for th in table.find('thead').find_all('th')]  # En-têtes des colonnes
rows = []
for tr in table.find('tbody').find_all('tr'):
    row = [td.text.strip() for td in tr.find_all(['th', 'td'])]
    rows.append(row)

# Création d'un DataFrame pandas
df = pd.DataFrame(rows, columns=headers)

# Spécifiez le dossier de sauvegarde
save_folder = r"C:\Users\marti\Desktop\dataof\City_predict"  # Utilisez "r" pour les chemins Windows
os.makedirs(save_folder, exist_ok=True)  # Crée le dossier s'il n'existe pas

# Sauvegarde du fichier CSV
csv_file = os.path.join(save_folder, "manchester_city_matches.csv")
df.to_csv(csv_file, index=False)

print(f"Données extraites et enregistrées dans : {csv_file}")

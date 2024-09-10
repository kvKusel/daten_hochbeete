import requests
import pandas as pd
import os 
import json


################################################            Bitte diesen Teil (urls, api key und value) ergänzen          ############################################################

# Liste der API-Endpunkte und zugehörigen Dateinamen - mit den richtigen URLs ersetzen!
url_file_mapping = {
    'https://XXX': 'Wetterdaten',
    'https://XXX': 'Kohlarabi',
    'https://XXX': 'Beethoven',
    'https://XXX': 'Wachstnix',
    'https://XXX': 'Kompostplatz_1',
    'https://XXX': 'Uebersee',
    'https://XXX': 'Shoppingqueen'
}

# AWS-Schlüssel und Werte einfügen
aws_access_key = 'XXX'
aws_secret_key = 'XXX'

# Authentifizierungs-Header erstellen
headers = {aws_access_key: aws_secret_key}

################################################                        Anfang des Programms                   ############################################################

# Loop durch die URL-Dateiname-Zuordnung
for url, filename in url_file_mapping.items():
    # API-Anfrage senden
    response = requests.get(url, headers=headers)
    
    # JSON-Daten abrufen
    data = response.json()
    
    # Den 'body'-Inhalt extrahieren und als JSON parsen
    body_data = json.loads(data['body'])
    
    # Daten in einen Pandas-DataFrame umwandeln
    df = pd.DataFrame(body_data)
    
    # DataFrame im Terminal anzeigen
    print(df)
    
    # Pfad zum Speichern der CSV-Datei angeben
    path = 'X:/XXX/XXX'
    csv_datei = os.path.join(path, f'{filename}.csv')  # Speichern unter Dateinamen
        
    # DataFrame als CSV speichern, Encoding latin-1 für deutsche Spezialzeichen 
    df.to_csv(csv_datei, index=False, encoding='latin-1')
    
    print(f'Daten von {url} in {csv_datei} gespeichert.\n')

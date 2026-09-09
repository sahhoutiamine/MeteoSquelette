import requests
import pandas as pd
import numpy as np
import json

def recuperer_donnees_meteo():
    """
    Étape 1 (Extract) : Se connecter à l'API pour récupérer les données.
    """
    print("⏳ Connexion à l'API en cours...")
    
    # URL de l'API Open-Meteo pour Casablanca (Températures max et min des 7 derniers jours)
    url = "https://api.open-meteo.com/v1/forecast?latitude=33.5883&longitude=-7.6114&past_days=7&daily=temperature_2m_max,temperature_2m_min&timezone=Africa%2FCasablanca"
    
    try:
        # --- TON CODE ICI : Utilise la bibliothèque 'requests' pour faire un 'get' sur l'url ---
        reponse = ... 
        
        # --- TON CODE ICI : Convertis la réponse au format '.json()' ---
        donnees_brutes = ...
        
        print("✅ Données récupérées avec succès depuis internet !")
        return donnees_brutes

    except Exception as e:
        print("❌ Erreur de connexion :", e)
        print("⚠️ Utilisation du fichier de secours (donnees_secours.json)...")
        
        # FILETS DE SÉCURITÉ : Si pas d'internet, on lit le fichier local
        with open("donnees_secours.json", "r") as fichier:
            return json.load(fichier)


def nettoyer_donnees(donnees_brutes):
    """
    Étape 2 (Transform) : Convertir le dictionnaire (JSON) en DataFrame Pandas.
    """
    print("⏳ Nettoyage des données avec Pandas...")
    
    # Dans le JSON de l'API, les infos utiles sont cachées dans la clé 'daily'
    donnees_utiles = donnees_brutes['daily']
    
    # --- TON CODE ICI : Transforme le dictionnaire 'donnees_utiles' en un DataFrame Pandas ---
    df = ...
    
    # On renomme les colonnes pour que ce soit plus clair (C'est cadeau !)
    df.columns = ['Date', 'Temp_Max', 'Temp_Min']
    
    return df


def afficher_statistiques(df):
    """
    Étape 3 : Utiliser NumPy pour faire des calculs sur notre DataFrame.
    """
    print("\n📊 --- STATISTIQUES DE LA SEMAINE ---")
    
    # --- TON CODE ICI : Utilise numpy (np) pour calculer la moyenne (mean) de la colonne 'Temp_Max' ---
    moyenne_max = ...
    
    # --- TON CODE ICI : Utilise numpy pour trouver la valeur maximale (max) de la colonne 'Temp_Max' ---
    pic_chaleur = ...
    
    print(f"👉 Température maximale moyenne : {moyenne_max:.2f}°C")
    print(f"👉 Pic de chaleur de la semaine : {pic_chaleur}°C\n")


def exporter_vers_csv(df, nom_fichier="meteo_casablanca.csv"):
    """
    Étape 4 (Load) : Sauvegarder le résultat de notre travail.
    """
    print(f"⏳ Sauvegarde en cours vers {nom_fichier}...")
    
    # --- TON CODE ICI : Utilise la méthode Pandas pour exporter 'df' en CSV. 
    # N'oublie pas l'argument index=False pour ne pas exporter les numéros de lignes ---
    ...
    
    print("✅ Sauvegarde terminée. Beau travail !")


# =====================================================================
# LE MOTEUR DU SCRIPT (Ne pas modifier cette partie)
# C'est ici que l'on appelle nos fonctions dans le bon ordre.
# =====================================================================
if __name__ == "__main__":
    print("🚀 Démarrage du Pipeline ETL Météo...\n")
    
    # 1. Extraction
    data_json = recuperer_donnees_meteo()
    
    if data_json:
        # 2. Transformation
        dataframe = nettoyer_donnees(data_json)
        
        # 3. Analyse
        afficher_statistiques(dataframe)
        
        # 4. Chargement (Sauvegarde)
        exporter_vers_csv(dataframe)
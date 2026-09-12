import requests
import pandas as pd
import numpy as np
import json


def recuperer_donnees_meteo():
    """
    Étape 1 (Extract) : Se connecter à l'API pour récupérer les données.
    """
    print("⏳ Connexion à l'API en cours...")

    # URL de l'API Open-Meteo pour Casablanca
    url = "https://api.open-meteo.com/v1/forecast?latitude=33.5883&longitude=-7.6114&past_days=7&daily=temperature_2m_max,temperature_2m_min&timezone=Africa%2FCasablanca"

    try:
        reponse = requests.get(url)

        if reponse.status_code != 200:
            raise Exception(f"Erreur HTTP : {reponse.status_code}")

        # Conversion de la réponse en JSON
        donnees_brutes = reponse.json()

        print("✅ Données récupérées avec succès depuis internet !")
        return donnees_brutes

    except Exception as e:
        print("❌ Erreur de connexion :", e)
        print("⚠️ Utilisation du fichier de secours (donnees_secours.json)...")

        # FILET DE SÉCURITÉ
        with open("donnees_secours.json", "r") as fichier:
            return json.load(fichier)


def nettoyer_donnees(donnees_brutes):
    """
    Étape 2 (Transform) : Convertir le dictionnaire (JSON) en DataFrame Pandas.
    """
    print("⏳ Nettoyage des données avec Pandas...")

    # Les données utiles sont dans la clé "daily"
    donnees_utiles = donnees_brutes["daily"]

    # Création du DataFrame
    df = pd.DataFrame(donnees_utiles)

    # Vérification
    if df.empty:
        raise Exception("Le DataFrame est vide.")

    # Renommer les colonnes
    df.columns = ["Date", "Temp_Max", "Temp_Min"]

    return df


def afficher_statistiques(df):
    """
    Étape 3 : Utiliser NumPy pour faire des calculs sur notre DataFrame.
    """
    print("\n📊 --- STATISTIQUES DE LA SEMAINE ---")

    # Conversion en tableau NumPy
    temperatures = df["Temp_Max"].values

    # Calculs avec NumPy
    moyenne_max = np.mean(temperatures)
    pic_chaleur = np.max(temperatures)

    print(f"👉 Température maximale moyenne : {moyenne_max:.2f}°C")
    print(f"👉 Pic de chaleur de la semaine : {pic_chaleur:.1f}°C\n")


def exporter_vers_csv(df, nom_fichier="meteo_casablanca.csv"):
    """
    Étape 4 (Load) : Sauvegarder le résultat de notre travail.
    """
    print(f"⏳ Sauvegarde en cours vers {nom_fichier}...")

    # Export du DataFrame vers un fichier CSV
    df.to_csv(nom_fichier, index=False)

    print("✅ Sauvegarde terminée. Beau travail !")


# =====================================================================
# LE MOTEUR DU SCRIPT (Ne pas modifier cette partie)
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
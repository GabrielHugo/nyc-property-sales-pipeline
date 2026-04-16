import mysql.connector
import time
import os

db_password = os.getenv("MOT_DE_PASSE_DB")

max_tries = 10
compteur = 0
conn = None

while compteur < max_tries:
    try:
        print(f"Test de connexion ({compteur + 1}/{max_tries})")
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password=db_password,
            database="myc-property-sales-pipeline"
        )

        print("Le conteneur Python est connecté au conteneur MySQL")
        break

    except Exception as e:
        print(f"MySQL n'est pas encore prêt", e)
        time.sleep(5)
        compteur += 1

if conn:
    conn.close()
else:
    print("Impossible de se connecter")
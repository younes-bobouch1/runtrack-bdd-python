import mysql.connector

#plugin
plug = mysql.connector.connect(
    user="root",
    password="root",
    database="laplateforme",
)

#check plugin (is_connected = verif connexion)
if plug.is_connected():
    print("Connexion réussie à la BDD.")

#connexion faite, maintenant récup data

#je crée mon curseur (executeur commande sql)
request = plug.cursor()

#commande de récupération, commande sql
request.execute("select superficie from etage;")

#var total_superficie
total_superficie = 0

#calcul
for superficie in request:
    total_superficie += superficie[0]

#affichage valuer
print(f"La superficie de La Plateforme est de {total_superficie} m2")

plug.close()
request.close()

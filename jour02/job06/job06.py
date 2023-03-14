import mysql.connector

plug = mysql.connector.connect (
    user = "root",
    password = "root",
    database = "laplateforme",
)

if plug.is_connected():
    print("Connexion à la BDD réussie.")

request = plug.cursor()

request.execute("select capacite from salles;")

capacite_salles = 0

for nb_salles in request:
    capacite_salles += nb_salles [0]

print(f"La capacité de toutes les salles est de : {capacite_salles}")

plug.close()
request.close()
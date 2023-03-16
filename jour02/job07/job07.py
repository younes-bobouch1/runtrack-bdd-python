import mysql.connector

#ma classe
class Crud:
    #connexion à ma bdd
    def __init__(self, user, password, database):
        self.plug = mysql.connector.connect(
            user = user,
            password = password,
            database = database,
        )
        self.cursor = self.plug.cursor()
        print("Connexion à la BDD réussie.")

    #méthode création data
    def crea(self, id, nom, prenom, salaire, id_service):
        sql = "insert into employes (id, nom, prenom, salaire, id_service) values (%s, %s, %s, %s, %s)"
        values = (id, nom, prenom, salaire, id_service)
        self.cursor.execute(sql, values)
        self.plug.commit()

    #méthode pour lire ma table, ici ma condition correspond à l'id
    def lire(self, condition=None):
        sql = "select * from employes"
        if condition:
            sql += f" where {condition}"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    #méthode pour changer des lignes, ici ma condition correspond à l'id
    def maj(self, colonne, valeur, condition):
        sql = f"update employes set {colonne} = %s where {condition}"
        values = (valeur,)
        self.cursor.execute(sql, values)
        self.plug.commit()

    #méthode pour del une valeur dans employes, ici ma condition correspond à l'id
    def dele(self, condition):
        sql = f"delete from employes where {condition}"
        self.cursor.execute(sql)
        self.plug.commit()

#marche
crud = Crud(user="root", password="root", database='societe')

#marche (mr poopy le pauvre, 20$ par mois)
#crud.crea(id=4, nom="Mister", prenom="Poopy", salaire=20.00, id_service=4)

result = crud.lire()
print(result)

#marche, (on rajoute 2$ à mr poopy le pauvre)
#crud.maj(colonne='salaire', valeur=22, condition='id=4')

#marche
#crud.dele(condition='id=5')







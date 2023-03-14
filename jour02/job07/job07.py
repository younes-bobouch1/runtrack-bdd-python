import mysql.connector

#ma classe
class Crud:
    #connexion à ma bdd
    def __init(self, user, password, database):
        self.plug = mysql.connector.connect(
            user = user,
            password = password,
            database = database,
        )
        self.cursor = self.plug.cursor

    def c(self, nom, prenom):
        sql = "insert into employes"

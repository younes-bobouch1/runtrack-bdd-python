class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def sesese(self):
        print( "jmp", self.nom, "et j'ai", self.age,)

one = Personne("Piero", 20)
two = Personne("Soli", 80)

one.sesese()
two.sesese()
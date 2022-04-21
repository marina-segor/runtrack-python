
from personne import Personne

class Auteur(Personne):
    def __init__(self, nom, prenom, age, collection: list):
        super().__init__(nom, prenom)
        self.age = age
        self.collection = collection

    def ecrireUnLivre(self, oeuvres):
        self.collection.append(oeuvres) 

    def ListeOeuvres(self):
        return self.collection
        
    def getAge(self, age):
        return self.age

    def setAge(self, age):
        self.age = age

    def afficherAuteur(nom, prenom, age, oeuvres):
        print(nom, prenom, age)

    def getOeuvres(self, oeuvres):
        return self.oeuvres
    
    def setOeuvres(self, oeuvres):
         self.oeuvres

    # oeuvres = []
    # oeuvres.append("chat")
    # print(oeuvres)


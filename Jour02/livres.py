#obj.show()
from auteur import Auteur

class Livres:
    def __init__(self, Auteur, titre):
        self.titre = titre
        self.Auteur = Auteur

    def getTitre(self, titre):
        return self.titre 


    def setTitre(self, titre):
        self.titre = titre

    def afficheLivre(self):
        print(self.titre)
  



    

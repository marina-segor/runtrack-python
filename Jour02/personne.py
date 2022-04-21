class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def setNom(self, nom):
        self.nom = nom

    def setPrenom(self, prenom):
        self.prenom = prenom

    def getNom(self, nom):
        return self.nom 

    def getPrenom(self, prenom):
        return self.prenom 

    def sePresenter(nom, prenom):
        print("Bonjour", nom, prenom)
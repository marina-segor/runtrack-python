from auteur import Auteur
from livres import Livres

# on déclare les auteurs 
auteur1 = Auteur("Piou", "pioupiou", 69, [])
auteur2 = Auteur("Marina", "Segor", 32, [])

# on déclare les titres et auteur livres
auteur1_livre1 = Livres(auteur1, "lululu")
auteur1_livre2 = Livres(auteur1, "blabla")

auteur2_livre1 = Livres(auteur2, "weshmec")
auteur2_livre2 = Livres(auteur2, "les miserables")


# on ajoute à liste des oeuvres
auteur1.ecrireUnLivre(auteur1_livre1.titre)
auteur1.ecrireUnLivre(auteur1_livre2.titre)

auteur2.ecrireUnLivre(auteur2_livre1.titre)
auteur2.ecrireUnLivre(auteur2_livre2.titre)


# on print 
print(auteur1.ListeOeuvres())
print(auteur2.ListeOeuvres())


#auteur1.AddOeuvre("blabla")
#print(auteur1.nom, auteur1.prenom)
# livre1 = Livres(auteur1, "monmoda")
#print(livre1.Auteur.prenom)
#Auteur.ListOeuvre(livre1.titre)    
#print(auteur2.ListeOeuvres())
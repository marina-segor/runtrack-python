from itertools import permutations

lettres_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
"k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print("Rentre un mot à transformer")
mot = input()
mot = mot.replace(" ", "")
mot = mot.lower()
for lettre in mot:
    if lettre not in lettres_alphabet:
        print("Erreur: le mot ne doit comporter que des lettres sans accent")
        exit()

len_mot = len(mot)

liste_combinaisons = list(permutations(mot, len_mot))
liste_combinaisons.sort()
mot_liste = tuple(list(mot))
index = liste_combinaisons.index(mot_liste)
del liste_combinaisons[0:index]
resultat = ''.join(liste_combinaisons[1])

print(resultat)


def arrondit_note(liste_notes):
    liste_resultat = []
    for note in liste_notes:
        if int(note) < 40:
            resultat = note
        else:
            unite = int(note[-1])
            if unite % 5 < 3:
                resultat = note
            else:
                decimale = note[-2]
                if not decimale:
                    decimale = "1"
                elif unite > 5:
                    decimale = str(int(decimale) + 1)
                if unite < 5:
                    resultat = note[:-2] + decimale + "5"
                else:
                    resultat = note[:-2] + decimale + "0"
        liste_resultat.append(resultat)
    return liste_resultat


def cree_liste():
    iterate = True
    liste_notes = []
    print("Rentre une liste de notes à arrondir au prochain multiple de 5")
    while iterate:
        print("Rentre une note à arrondir ou", "stop", "pour arrêter et créer la liste")
        note = input()
        if note == "stop":
            iterate = False
        else:
            try:
                int(note)
            except ValueError:
                print("Erreur : Rentre un nombre entier ou", "stop", "pour arrêter")
                continue
            liste_notes.append(note)
    liste_resultat = arrondit_note(liste_notes)
    for note in liste_resultat:
        print(note)


cree_liste()

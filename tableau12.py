def recherche(liste, valeur):
    for i in range(len(liste)):
        if liste[i] == valeur:
            return liste.remove(valeur)
    return -1
liste = [20, 8, 9, 2, 35, 49]
valeur = 49
print(recherche(liste, valeur))
print(liste)
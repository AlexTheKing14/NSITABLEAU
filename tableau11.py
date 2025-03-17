def recherchemin(liste):
    min = liste[0]
    for i in range(1, len(liste)):
        if liste[i] < min:
            min = liste[i]
    return min

def recherchemax(liste):
    max = liste[0]
    for i in range(1, len(liste)):
        if liste[i] > max:
            max = liste[i]
    return max

def somme(liste):
    somme = 0
    for i in range(0, len(liste)):
        somme += liste[i]
    return somme

def moyenneV2(liste):
    moyenne = somme(liste) / len(liste)
    return moyenne

liste = [20, 8, 9, 2, 35, 49]
def rechercheminmaxmyenne(liste):
    tuple = (recherchemin(liste), recherchemax(liste), moyenneV2(liste))
    return tuple
print(rechercheminmaxmyenne(liste))
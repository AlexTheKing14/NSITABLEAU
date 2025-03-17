def somme(liste):
    somme = 0
    for i in range(0, len(liste)):
        somme += liste[i]
    return somme

def moyenneV2(liste):
    moyenne = somme(liste) / len(liste)
    return moyenne
liste = [20, 8, 9, 2, 35, 49]
print(moyenneV2(liste))
def somme(liste):
    somme = 0
    for i in range(0, len(liste)):
        somme += liste[i]
    return somme
liste = [20, 8, 9, 2, 35, 49]
print(somme(liste))
def moyenneV1(liste):
    total = 0 
    for i in range(len(liste)):
        total = total + liste[i]
    total = total / len(liste)
    return total
liste = [20, 8, 9, 2, 35, 49]
print(moyenneV1(liste))
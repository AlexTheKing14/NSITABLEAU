tab = [3, 7, 2, 9, 4]
print(tab)

print(tab[0])
print(tab[4])
print(tab[2])

tab[1] = 15
tab.append(12)
tab.insert(1, 5)

tab.pop(0)
tab.pop(3)

print(len(tab))
print("___")
for indice in tab:
    print(indice)
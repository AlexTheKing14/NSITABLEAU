n = 0
chaine = str(input("Entrez une chaîne de caractères : "))
for i in chaine:
    if i == "e":
        n += 1
    else:
        print("Pas de E")
print(n)
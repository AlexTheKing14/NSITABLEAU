dico_hobbit = {"prenom" : "Bilbon", "Age" : 111}
dico_hobbit ["nom"] = "Sacquet"

dico_hobbit["Age"] = 131
print(dico_hobbit)

print("____________")

for cle in dico_hobbit:
    print(cle)

print("____________")

for val in dico_hobbit.values():
    print(val)

print("____________")

for (cle, val) in dico_hobbit.items():
    print(cle, "->", val)
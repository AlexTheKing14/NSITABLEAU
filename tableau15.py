dico_classe = {}
nombre = int(input("Entrez un nombre d'étudiant : "))

for i in range(nombre):
    nom = input("Entrez le nom de l'étudiant : " )
    age = input("Entrez l'âge de l'étudiant : " )
    dico_classe[nom] = age

print("Dictionnaire des étudiants : ")
for nom, age in dico_classe.items():
    print(nom, age)


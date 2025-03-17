dico_classe = {"Alexandre" : 16, "Nolan" : 16, "Baptiste" : 16, "Marin" : 16, "Arthur" : 16}
nom = input("Entrez le nom de l'étudiant : ")

def existeoupas(nom):
    if nom in dico_classe:
        print("L'élève existe déjà, changement de l'âge")
        age = int(input("Entrez l'âge de l'étudiant : "))
        dico_classe[nom] = age
    else:
        print("L'élève n'existe pas, ajout de l'élève")
        age = int(input("Entrez l'âge de l'étudiant : "))
        dico_classe[nom] = age
existeoupas(nom)
print("Dictionnaire des étudiants : ")
for nom, age in dico_classe.items():
    print(nom, age)
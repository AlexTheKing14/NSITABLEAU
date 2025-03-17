dico_classe = {"Alexandre" : 16, "Nolan" : 16, "Baptiste" : 16, "Marin" : 16, "Arthur" : 16}
nom = input("Entrez le nom de l'élève : ")

def recherche(nom):
    if nom in dico_classe:
        print("Âge de l'élève :", dico_classe[nom])
    else:
        print("Non trouvé")

recherche(nom)
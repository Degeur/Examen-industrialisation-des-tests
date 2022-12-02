import csv
import random
dico_couleur={0: "\033[34m", 1 : "\033[31m", 2 : "\033[32m", 3 : "\033[35m", 4 : "\033[39m", 5: "\033[34m", 6 : "\033[31m", 7 : "\033[32m", 8 : "\033[35m", 9 : "\033[39m"}



def charger():
    with open('abilities.csv', newline='') as fichier:
        lecture = csv.reader(fichier, delimiter=',')
        lignes = list(lecture)
    return lignes


def extraire(lignes):
    liste_objets=[]
    global liste_nombre
    liste_nombre = []
    for i in range (10):
        nombre = random.randint(0, len(lignes))
        liste_objets.append(lignes[nombre])
        liste_nombre.append(nombre)
    return liste_objets

def afficher(liste_objets):
    for i in range (10):
        print("La ligne", liste_nombre[i], " du fichier:", liste_objets[i], dico_couleur[i])



lignes = charger()
liste_objets = extraire(lignes)
afficher(liste_objets)

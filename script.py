import csv
import random
dico_couleur={0: "\033[34m", 1 : "\033[31m", 2 : "\033[32m", 3 : "\033[35m", 4 : "\033[39m", 5: "\033[34m", 6 : "\033[31m", 7 : "\033[32m", 8 : "\033[35m", 9 : "\033[39m"}
liste_objets=[]


def charger():
    with open('abilities.csv', newline='') as fichier:
        global lecture
        global lignes
        lecture = csv.reader(fichier, delimiter=',')
        lignes = list(lecture)


def extraire():
    global i
    global lignes
    global nombre
    for i in range (10):
        nombre = random.randint(0, len(lignes))
        liste_objets.append(lignes[nombre])

def afficher():
    for i in range (10):
         print("La ligne", nombre, " du fichier:", liste_objets[i], dico_couleur[i])



charger()
extraire()
afficher()

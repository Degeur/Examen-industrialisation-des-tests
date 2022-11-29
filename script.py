import csv
import random

class color:
    g = '\033[92m' # vert
    y = '\033[93m' # jaune
    r = '\033[91m' # rouge
    n = '\033[0m' #gris, couleur normale

with open('abilities.csv', newline='') as fichier:
    lecture = csv.reader(fichier, delimiter=',')
    lignes = list(lecture)

dico_couleur={0: "\033[34m", 1 : "\033[31m", 2 : "\033[32m", 3 : "\033[35m", 4 : "\033[39m", 5: "\033[34m", 6 : "\033[31m", 7 : "\033[32m", 8 : "\033[35m", 9 : "\033[39m"}

for i in range (10):
    nombre = random.randint(0, len(lignes))
    print("La ligne", nombre, " du fichier:", lignes[nombre], dico_couleur[i])

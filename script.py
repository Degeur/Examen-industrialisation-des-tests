import csv
import random
with open('abilities.csv', newline='') as fichier:
    lecture = csv.reader(fichier, delimiter=',')
    lignes = list(lecture)
for loop in range (10):
    nombre = random.randint(0, len(lignes))
    print(f"La ligne", nombre, " du fichier:", lignes[nombre])

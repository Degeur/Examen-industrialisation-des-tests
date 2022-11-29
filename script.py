import csv
# ouverture en lecture du fichier csv
with open('abilities.csv', newline='') as fichier:
    # on crée un objet reader
    lecture = csv.reader(fichier, delimiter=',')

    # lecture et affichage des lignes:
    for ligne in lecture:
        print(ligne)
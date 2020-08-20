from random import *
# un jeu de carte
couleur=["pique", "coeur", "carreau", "trèfle"]
hauteur = ["As", "Roi", "Dame", "Valet", "Dix", "Neuf", "Huit", "Sept"]
#Au total le jeu compte 32 cartes
jeu = []
for c in couleur:
    for h in hauteur:
        jeu.append(h+" :-----:::))) "+c)
print("----------------------------LE NOUVEAU JEU----------------------------")
print("\n".join(jeu))

# mélanger
shuffle(jeu)
print("--------------------------Le jeu mélangé----------------------------------------")
print("\n".join(jeu))


# Choisir au hasard le nombre de carte à donner
N = randint(3, 10)
print("Je donne "+str(N)+" cartes")

# Donner N cartes
donne = sample(jeu, N)
print("Les voilà :")
print(donne)
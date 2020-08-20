class Humaine:
    '''méthode de class'''
    lieu="UCAD"
    nombrePersoCrer = 0
    def __init__(self, class_prenom, class_age):
        self.prenom = class_prenom
        self.age = class_age
    nombrePersoCrer=nombrePersoCrer+ 1
    def parler(self,message):
        print(self.prenom," a dit: {}".format(message))
'''
    def place(cls,lieu):
        Humaine.lieu = lieu
    place=classmethod(place())
'''

print("Lancement du programme...");
h1 = Humaine("khadim", 21)
h1.parler("Hello every body")
print("vous vous appelé ", h1.prenom, " et tu as {}".format(h1.age), " ans")
'''
Humaine.lieu="UCAD TDSI"
Humaine.place(Humaine.lieu)
'''

print("Le nombre de personne crées est: {} ".format(h1.nombrePersoCrer))
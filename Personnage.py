"""
Création d'une classe Personnage permettant l'export d'un objet JSON
"""

import json


class Personnage:
    def __init__(self, nom: str, prenom: str) -> None:
        self.nom = nom
        self.prenom = prenom

    def getIdentity(self):
        return self.nom, self.prenom

    def toJSON(self):
        # La méthode magique __dict__ transforme l'objet en dictionnaire (?)
        return json.dumps(self.__dict__)


"""
Tests sur la classe Personnage
"""
moi = Personnage("PAIN-CHAMMING'S", "Jonathan")  # Création d'un objet
print('Sortie de la méthode getIdentity() :\n', moi.getIdentity())
print('Sortie de la méthode toJSON() :\n', moi.toJSON())

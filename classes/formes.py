class Rectangle(object):
    "Classe de rectangles"

    def __init__(self, longueur=0, largeur=0):
        self.longueur = longueur
        self.largeur = largeur
        self.nom = "rectangle"

    def perimetre(self) -> str:
        return f"({self.longueur} + {self.largeur}) * 2 = {(self.longueur + self.largeur) * 2}"

    def surface(self) -> str:
        return f"{self.longueur} * {self.largeur} = {self.longueur * self.largeur}"

    def mesures(self):
        print(f"Un {self.nom} de {self.longueur} sur {self.largeur}")
        print(f"a une surface de {self.surface()}")
        print(f"et un périmètre de {self.perimetre()}\n")


class Carre(Rectangle):
    "Classe de carrés"

    def __init__(self, cote):
        Rectangle.__init__(self, cote, cote)
        self.nom = "carré"


if __name__ == "__main__":
    r1 = Rectangle(15, 30)
    r1.mesures()
    c1 = Carre(13)
    c1.mesures()

# Exercice de création de classes simples en Python
import math


class Point(object):
    """Définition d'un point géométrique :
    La classe est Modifiée afin de retourner les coordonnées
    du point lors du passage d'un de ses objets en print()"""
    def __str__(self) -> str:
        return f"X : {self.x}, Y : {self.y}"

class Rectangle(object):
    "Définition d'un rectangle"

def display_point(p: Point) -> None:
    "Affiche les coordonées d'un objet Point"
    print("Appel de la fontion display_point avec l'argument", p)
    print("Coordonnée horizontale :", p.x, "\nCoordonnée verticale :", p.y)


def distance(p1: Point, p2: Point) -> float:
    "Calcule la distance entre deux point en utilisant le théorème de Pythagore"
    hypotenus = (p1.x-p2.x)**2 + (p1.y-p2.y)**2
    return math.sqrt(hypotenus)


p9 = Point()
p0 = Point()

# Passage d'attributs à l'objet p9
# c'est possible de faire ça en Python mais ça reste sale
p9.x = 8.4
p9.y = 5.5

print(p9.__doc__, p9.__str__.__doc__)

p0.x, p0.y = 0, 0
print("Attribution de variables à l'objet p9 via les commandes :\np9.x = 3.0 et p9.y = 4.0")

print("p9.x ** 2 + p9.y ** 2 est égale à :", p9.x ** 2 + p9.y ** 2)

display_point(p9)
print("Résultat de la function distance() p0 et p9", distance(p0, p9))
print(p0)

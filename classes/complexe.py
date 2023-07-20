# Exercice de création de classe complexe en Python
from datetime import datetime


class Time(object):
    "Définition d'objets temporels"

    def __init__(self, h=datetime.now().hour, m=datetime.now().minute, s=datetime.now().second) -> None:
        # now = datetime.now()
        self.heure = h
        self.minute = m
        self.seconde = s

    def display_time(self) -> None:
        print(f"{self.heure}:{self.minute}:{self.seconde}")


class Domino(object):
    "Définition d'objets domino, disposant d'une face A et d'une face B"

    def __init__(self, a: int = 0, b: int = 0) -> None:
        self.a = a
        self.b = b

    def display_points(self) -> None:
        print("┌───┬───┐")
        print(f"├ {self.a} ┼ {self.b} ┤")
        print("└───┴───┘")

    def value(self) -> int:
        return self.a + self.b


class Satellite(object):
    "Définition d'objets satellites disposant d'un nom, d'une masse et d'une vitesse"

    def __init__(self, name: str, mass: int = 100, speed: float = 0) -> None:
        self.name = name
        self.mass = mass
        self.speed = speed

    def impulse(self, force: int, time: int) -> None:
        accelerate = force * time / self.mass
        self.speed += accelerate

    def display_speed(self) -> None:
        print(f"Vitesse du satellite \"{self.name}\" = {self.speed} m/s")

    def energy(self) -> float:
        return self.mass * (self.speed ** 2) / 2


class Espaces(object):
    aa = 33

    def affiche(self):
        print(aa, Espaces.aa, self.aa)


# Test sur Time()
print("\nTest sur Time()")
print('===============')
instant = Time()
instant.display_time()

# Test sur Dommino()
print("\nTest sur Dommino()")
print('==================')
d1 = Domino(2, 6)
d2 = Domino(4, 3)

d1.display_points()
d2.display_points()

print("Total des points :", d1.value() + d2.value())

# Test sur Satellite()
print("\nTest sur Satellite()")
print('====================')
s1 = Satellite("Zoé", 250, 10)
s1.impulse(500, 15)
s1.display_speed()

print(s1.energy())

s1.impulse(500, 15)
s1.display_speed()

print(s1.energy())


# Test sur Espaces()
print("\nTest sur Espaces()")
print('==================')
aa = 12

essai = Espaces()
essai.aa = 67
essai.affiche()

print(aa, Espaces.aa, essai.aa)

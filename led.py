"""
# Programme domotique avec Raspberry
Un bouton permet de faire clignoter la LED et sonner le buzzer.
Un second bouton permet d'arrêter le programme et réinitialiser le Raspberry
"""

import RPi.GPIO as gpio # Chargement de la bibliothèque pour le Raspberry
from time import sleep

# Initialisation du Raspberry
gpio.setmode(gpio.BOARD) # Initialisation du mode BOARD
gpio.setup(3,gpio.OUT) # Initialisation de la broche 3 en sortie (LED)
gpio.setup(16,gpio.OUT) # Initialisation de la broche 16 en sortie (Buzzer)
gpio.setup(7,gpio.IN) # Initialisation de la broche 7 en entrée (Bouton Start)
gpio.setup(11,gpio.IN) # Initialisation de la broche 7 en entrée (Bouton Reset)


"""
# Lecture/Assignatin des états
gpio.input(7) # Lecture de la valeur de la broche 7
gpio.output(3,gpio.HIGH) # Assignation d’une valeur à la broche 3 (LED allumée)
gpio.output(3,gpio.LOW) # Assignation d’une valeur à la broche 3 (LED éteinte)
"""

def main():
    gpio.output(3,gpio.LOW)
    gpio.output(16,gpio.LOW)
    print('Programme lancé, prêt à clignoter !')
    while True:
        if not gpio.input(7):
            blink()

def ledON ():
    gpio.output(3,gpio.HIGH)
    gpio.output(16,gpio.LOW)
    return print('La LED est allumée')

def ledOFF ():
    gpio.output(3,gpio.LOW)
    gpio.output(16,gpio.HIGH)
    return print('La LED est étinte')

def blink ():
    while gpio.input(11):
        ledON()
        sleep(0.05)
        ledOFF()
        sleep(0.05)
    gpio.cleanup()
    print('Programme arrété')
    exit(0)

if __name__ == "__main__":
    main()
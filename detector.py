"""
Programme domotique avec Raspberry - Veilleuse de nuit
Une photorésistance déclenche l'allumage d'une LED jaune
Un premier bouton permet de lancer le programme
Un second bouton permet d'arrêter le programme et réinitialiser le Raspberry
"""

import RPi.GPIO as gpio # Chargement de la bibliothèque pour le Raspberry

# Initialisation du Raspberry
gpio.setmode(gpio.BOARD) # Initialisation du mode BOARD
gpio.setup(38,gpio.OUT) # Initialisation de la broche 38 en sortie (LED jaune)
gpio.setup(3,gpio.OUT) # Initialisation de la broche 38 en sortie (LED rouge)
gpio.setup(7,gpio.IN) # Initialisation de la broche 7 en entrée (Bouton Start - Default 1)
gpio.setup(11,gpio.IN) # Initialisation de la broche 11 en entrée (Bouton Reset - Default 1)
gpio.setup(40,gpio.IN) # Initialisation de la broche 40 en entrée (Photorésistance - Default 1)

previousState = 0

"""
# Lecture/Assignatin des états
gpio.input(7) # Lecture de la valeur de la broche 7
gpio.output(3,gpio.HIGH) # Assignation d’une valeur à la broche 3 (LED allumée)
gpio.output(3,gpio.LOW) # Assignation d’une valeur à la broche 3 (LED éteinte)
"""

def detector():
    while gpio.input(7) and gpio.input(11): # Arrêt du programme si on appuie sur un bouton
        if gpio.input(40):
            gpio.output(38, gpio.LOW)
            gpio.output(3, gpio.LOW)
            message(True)
        else:
            gpio.output(38, gpio.HIGH)
            gpio.output(3, gpio.HIGH)
            message(False)
    gpio.cleanup()
    print('Programme arrété')

def message(messageState):
    global previousState
    if messageState:
        messageToDisplay = 'Il fait jour.'
    else:
        messageToDisplay = 'Il fait nuit, lumière SVP !'
    if messageState != previousState:
        print(messageToDisplay)
        previousState = not previousState

def main():
    gpio.output(38,gpio.LOW)
    gpio.output(3,gpio.LOW)
    print('Programme lancé, en attente d\'instruction')
    detector()

if __name__ == "__main__":
    main()
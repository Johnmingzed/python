"""
Script de réinitialisation du Raspberry
"""

import RPi.GPIO as gpio # Chargement de la bibliothèque pour le Raspberry

# Initialisation du Raspberry
gpio.setmode(gpio.BOARD) # Initialisation du mode BOARD
gpio.setup(38,gpio.OUT) # Initialisation de la broche 38 en sortie (LED jaune)
gpio.setup(3,gpio.OUT) # Initialisation de la broche 38 en sortie (LED rouge)
gpio.setup(7,gpio.IN) # Initialisation de la broche 7 en entrée (Bouton Start - Default 1)
gpio.setup(11,gpio.IN) # Initialisation de la broche 7 en entrée (Bouton Reset - Default 1)
gpio.setup(40,gpio.IN) # Initialisation de la broche 40 en entrée (Photorésistance - Default 1)

# Réinitialisatoin des états du Raspberry et sortie du programme
gpio.cleanup()
exit('Raspberry réinitialisé')
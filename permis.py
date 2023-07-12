"""
Création d'un programme en ligne de commande utilisant les conditions if
"""

import sys


USAGE = f'Usage : python {sys.argv[0]} [age(int)]'
age_input = 0


def test_arguments():
    if len(sys.argv) > 2:
        sys.exit(USAGE)


def set_age():
    global age_input
    try:
        sys.argv[1]
    except:
        age_input = input('Quel âge as-tu ? \n')
    else:
        age_input = sys.argv[1]


def verif_age():
    global age_input
    try:
        age_input = int(age_input)
    except ValueError:
        exit("Merci d'indiquer un entier.")


def result():
    global age_input
    if age_input >= 70:
        print("À {} ans, il serait plus prudent de prendre le bus.".format(age_input))
    elif age_input >= 18:
        print("À %s ans, tu peux passer ton permis de conduire" % age_input)
    elif age_input >= 16:
        print("À " + str(age_input) +
            " ans, tu peux passer la conduite à accompagnée.")
    else:
        print(f"À {age_input} ans, mieux vaut rouler à vélo.")


def main():
    test_arguments()
    set_age()
    verif_age()
    result()
    exit(0)


if __name__ == "__main__":
    main()

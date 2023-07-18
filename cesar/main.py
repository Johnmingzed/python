from tkinter import *
from tkinter import filedialog
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")
os.chdir(data_dir)

root = Tk()
root.title("Super Chiffrement 3000")
menu_bar = Menu(root)
global file


def quitter():
    # Fonction pour quitter l'application
    root.destroy()


def ouvrir_fichier():
    # Fonction pour ouvrir le dialogue de sélection de fichier
    global file, file_path
    filetypes = (("Text files", "*.txt"), ("All files", "*.*"))
    file_path = filedialog.askopenfilename(filetypes=filetypes)
    print("Fichier séléctionné", file_path)
    if file_path:
        obFile = open(file_path, "r")
        file = obFile.read()
        obFile.close()
        # Afficher le contenu du fichier dans le widget Text
        displayText(file)


def displayText(text: str) -> None:
    text_area.delete("1.0", END)
    text_area.insert("1.0", text)


def chiffrer(inputText: str, step: int) -> str:
    outputText = ""
    cursor = 0
    while cursor <= len(inputText) - 1:
        asciiLetter = ord(inputText[cursor])
        asciiLetter += step
        cryptedLetter = chr(asciiLetter)
        outputText += cryptedLetter
        cursor += 1
    return outputText


def chiffrerTexte(step: int):
    text = text_area.get("1.0", END)
    print(text)
    output = chiffrer(text, step)
    displayText(output)


# Configuration de la barre de menu
root.config(menu=menu_bar)

# menu "Fichier"
menu_files = Menu(menu_bar, tearoff=0)
menu_files.add_command(label="Nouveau")
menu_files.add_command(label="Ouvrir", command=ouvrir_fichier)
menu_files.add_command(label="Enregistrer")
menu_files.add_separator()
menu_files.add_command(label="Exit", command=quitter)
menu_bar.add_cascade(label="Fichiers", menu=menu_files)

# menu "Aide"
menu_aide = Menu(menu_bar, tearoff=0)
menu_aide.add_command(label="À propos")
menu_bar.add_cascade(label="Aide")

# zone de texte
text_area = Text(root)
text_area.pack(fill=BOTH, expand=YES)

# Bouton chiffrement
encryptButton = Button(root, text="Chiffrer", command=lambda: chiffrerTexte(int(stepSelector.get())))
encryptButton.pack()

# Bouton déchiffrement
decryptButton = Button(root, text="Déchiffrer", command=lambda: chiffrerTexte(-int(stepSelector.get())))
decryptButton.pack()

# Selection du pas
stepSelector = Spinbox(root, from_=1, to=127)
stepSelector.pack()

# Affichage du fichier séléctionné
if 'file' in globals():
    text_area.insert("1.0", file)

# Rendu du programme
root.mainloop()

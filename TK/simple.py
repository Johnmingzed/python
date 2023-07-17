from tkinter import *

def main():
    # Création de la fenêtre
    fenetre = Tk()

    message = Label(fenetre, text="Salut Meufec, bienvenue dans ce programme", fg="#FF0000", pady=20, width=48, height=10)
    fermer = Button(fenetre, text="Quitter", command=fenetre.destroy)

    message.pack()
    fermer.pack()

    # Rendu de la fenêtre
    fenetre.mainloop()

if __name__ == "__main__":
    main()
from tkinter import *


def cercle(can, x, y, r, color=None):
    "Dessin d'un cercle de rayon <r> en <x,y> dans le canevas <can>"
    can.create_oval(x-r, y-r, x+r, y+r, fill=color)


class Application(Tk):
    def __init__(self):
        Tk.__init__(self)    # constructeur de la classe parente
        self.can = Canvas(self, width=475, height=130, bg="white")
        self.can.pack(side=TOP, padx=5, pady=5)
        Button(self, text="Train", command=self.dessine).pack(side=LEFT)
        Button(self, text="Hello", command=self.coucou).pack(side=LEFT)
        Button(self, text="Allumer", command=lambda: self.allumer_fenetres()).pack(side=LEFT)

    def allumer_fenetres(self):
        "changement de couleur des fenêtres"
        self.w1.allumer()
        self.w2.allumer()
        self.w3.allumer()
        self.w4.allumer()

    def dessine(self):
        "instanciation de 4 wagons dans le canevas"
        self.w1 = Wagon(self.can, 10, 30)
        self.w2 = Wagon(self.can, 130, 30)
        self.w3 = Wagon(self.can, 250, 30)
        self.w4 = Wagon(self.can, 370, 30)

    def coucou(self):
        "apparition de personnages dans certaines fenêtres"
        self.w1.perso(3)	      # 1er wagon, 3e fenêtre
        self.w3.perso(1)	      # 3e wagon, 1e fenêtre
        self.w3.perso(2)	      # 3e wagon, 2e fenêtre
        self.w4.perso(1)	      # 4e wagon, 1e fenêtre


class Wagon(object):
    def __init__(self, canev, x, y):
        "dessin d'un petit wagon en <x,y> dans le canevas <canev>"
        # mémorisation des paramètres dans des variables d'instance :
        self.canev, self.x, self.y = canev, x, y
        # rectangle de base : 95x60 pixels :
        canev.create_rectangle(x, y, x+95, y+60, fill='light blue')
        # 3 fenêtres de 25x40 pixels, écartées de 5 pixels :
        for xf in range(x+5, x+90, 30):
            canev.create_rectangle(xf, y+5, xf+25, y+40, fill='black', tags='fenetre')
        # 2 roues de rayon égal à 12 pixels  :
        cercle(canev, x+18, y+73, 12, 'grey')
        cercle(canev, x+77, y+73, 12, 'grey')

    def perso(self, fen):
        "apparition d'un petit personnage à la fenêtre <fen>"
        # calcul des coordonnées du centre de chaque fenêtre :
        xf = self.x + fen*30 - 12
        yf = self.y + 25
        cercle(self.canev, xf, yf, 10, 'pink')	  # visage
        cercle(self.canev, xf-5, yf-3, 2, 'black')   # oeil gauche
        cercle(self.canev, xf+5, yf-3, 2, 'black')   # oeil droit
        cercle(self.canev, xf, yf+5, 3, 'red4')	   # bouche

    def allumer(self):
        "changement de couleur des fenêtres <fen>"
        fenetres = self.canev.find_withtag('fenetre')
        for fenetre in fenetres:
            self.canev.itemconfig(fenetre, fill='yellow')


app = Application()
app.mainloop()

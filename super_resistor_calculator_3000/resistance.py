class Application(object):
    def __init__(self):
        """Constructeur de la fenêtre principale"""
        self.root = Tk()
        self.root.resizable(False, False)
        self.root.title('Super Resistor Calculator 3000')
        self.dessineResistance()
        Label(self.root, text="Entrez la valeur de la résistance, en ohms :").\
            grid(row=2, column=1, columnspan=3)
        Button(self.root, text='Effacer', command=self.videEntree).\
            grid(row=3, column=1)
        Button(self.root, text='Quitter', command=self.root.quit).\
            grid(row=3, column=3)
        self.entree = Entry(self.root, width=14)
        self.entree.bind("<Return>", self.changeCouleurs)
        self.entree.grid(row=3, column=2)
        self.li = [0]*3                 # Initialisation du code couleur de la résistance
        self.v1ch = self.entree.get()   # Initialisation de la valeur de la résistance
        # Code des couleurs pour les valeurs de zéro à neuf :
        self.cc = ['black', 'brown', 'red', 'orange', 'yellow',
                    'green', 'blue', 'purple', 'grey', 'white']
        self.root.mainloop()

    def dessineResistance(self):
        """Canevas avec un modèle de résistance à trois lignes colorées"""
        self.size_factor = 3    # Cette variable permet de modifier l'échelle du canvas
        self.can = Canvas(self.root, width=250*self.size_factor,
                            height=100*self.size_factor, bg='light blue')
        self.can.grid(row=1, column=1, columnspan=3, pady=5, padx=5)
        self.can.create_line(10*self.size_factor, 50*self.size_factor, 240*self.size_factor,
                                50*self.size_factor, width=3*self.size_factor)	       # fils
        self.can.create_rectangle(65*self.size_factor, 30*self.size_factor, 185 *
                                    self.size_factor, 70*self.size_factor, fill='beige', width=2*self.size_factor)
        # Dessin des trois lignes colorées (noires au départ) :
        self.ligne = []         # on mémorisera les trois lignes dans 1 liste
        for x in range(85*self.size_factor, 150*self.size_factor, 24*self.size_factor):
            bande_couleur = self.can.create_rectangle(x, 31*self.size_factor, x+16*self.size_factor, 69*self.size_factor,
                                            fill='black', width=0, tags='bande')  # Ajout du tag 'bande' ici
            self.ligne.append(bande_couleur)
            # On lie un évènement clic pour chaque bande
            self.can.tag_bind(bande_couleur, "<Button>", lambda event, rect_id=bande_couleur: self.choisirCouleur(event, rect_id))

    def changeCouleurs(self, *args):
        """Affichage des couleurs correspondant à la valeur entrée"""
        self.v1ch = self.entree.get()   # cette méthode renvoie une chaîne
        try:
            v = float(self.v1ch)        # conversion en valeur numérique
        except:
            err = 1		                # erreur : entrée non numérique
        else:
            err = 0

        if err == 1 or v < 1 or v > 1e11:
            self.signaleErreur()	    # entrée incorrecte ou hors limites
        elif v < 10:
            self.li = [0]*3
            v *= 10
            vstring = str(v).zfill(4)
            self.li[1] = int(vstring[0])
            self.li[2] = int(vstring[1])
            # Coloration des 3 lignes :
            self.coloration()
        else:
            self.li = [0]*3 	                # liste des 3 codes à afficher
            logv = int(log10(v))	            # partie entière du logarithme
            ordgr = 10**logv		            # ordre de grandeur
            # extraction du premier chiffre significatif :
            self.li[0] = int(v/ordgr)	        # partie entière
            decim = v/ordgr - self.li[0]	    # partie décimale
            # extraction du second chiffre significatif :
            # +.5 pour arrondir correctement
            self.li[1] = int(decim*10 + .5)
            # nombre de zéros à accoler aux 2 chiffres significatifs :
            self.li[2] = logv - 1
            # Coloration des 3 lignes :
            self.coloration()

    def coloration(self):
        """Applique la couleur à chaque bande selon le code couleur"""
        for n in range(3):
            self.can.itemconfigure(self.ligne[n], fill=self.cc[self.li[n]])

    def signaleErreur(self):
        self.entree.configure(bg='red')	        # colorer le fond du champ
        self.root.after(1000, self.videEntree)  # après 1 seconde, effacer

    def videEntree(self):
        self.entree.configure(bg='white')       # rétablir le fond blanc
        self.entree.delete(0, len(self.v1ch))
        self.li = [0, 0, 0]	                    # enlever les car. présents
        self.coloration()                       # réinitialiser les bandes

    def choisirCouleur(self, event, rect_id):
        x, y = event.x_root, event.y_root
        id_bande = rect_id
        self.popup = Toplevel()
        self.popup.geometry(f'150x150+{x}+{y}')
        self.popup.resizable(False,False)
        label = Label(self.popup, text="Choissez une couleur")
        label.pack()
        canvas = Canvas(self.popup, width=25*5+2, height=50*2+2, bg='white')
        for couleur in self.cc:
            i = self.cc.index(couleur)
            if i < 5:
                # Les valeurs de x et y sont modifiées afin de compenser le filet des rectangles
                canvas.create_rectangle(25*i+2, 50*0+2, 25+25*i+2, 50+2, fill=couleur, tags=couleur)
            else:
                # On décalle toutes les valeurs x et y afin de passer sur la deuxième ligne
                canvas.create_rectangle(25*i-123, 50+50*0+2, 25+25*i-123, 100+2, fill=couleur, tags=couleur)
            canvas.tag_bind(couleur, "<Button>", lambda event, couleur=couleur: self.assigneValeur(event, id_bande, couleur))
        canvas.pack(padx=5, pady=5)

    def assigneValeur(self, event, id_bande, couleur):
        self.popup.withdraw()
        for i in range(len(self.ligne)):
            if self.ligne[i] == id_bande:
                self.li[i] = self.cc.index(couleur)
        self.coloration()
        self.calculeValeur()

    def calculeValeur(self):
        if self.li[0] > 0:
            # La valeur sera >= 10
            valeur = (self.li[0] * 10 + self.li[1]) * (10 ** self.li[2])
        else:
            # La valeur sera < 10
            valeur = (self.li[1] * 10 + self.li[2]) / 10
        print('On calcule :', self.li, "ce qui donne :", valeur, "Ohms")
        self.v1ch = self.entree.get()
        self.entree.delete(0, len(self.v1ch))
        self.entree.insert(0, valeur) 


# Programme principal :
if __name__ == '__main__':
    from tkinter import *
    from math import log10  # logarithmes en base 10
    f = Application()	    # instanciation de l'objet application

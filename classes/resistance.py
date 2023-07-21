class Application(object):
    def __init__(self):
        """Constructeur de la fenêtre principale"""
        self.root = Tk()
        self.root.resizable(False, False)
        self.root.title('Code des couleurs')
        self.dessineResistance()
        Label(self.root, text="Entrez la valeur de la résistance, en ohms :").\
            grid(row=2, column=1, columnspan=3)
        Button(self.root, text='Montrer', command=self.changeCouleurs).\
            grid(row=3, column=1)
        Button(self.root, text='Quitter', command=self.root.quit).\
            grid(row=3, column=3)
        self.entree = Entry(self.root, width=14)
        self.entree.bind("<Return>", self.changeCouleurs)
        self.entree.grid(row=3, column=2)
        # Code des couleurs pour les valeurs de zéro à neuf :
        self.cc = ['black', 'brown', 'red', 'orange', 'yellow',
                'green', 'blue', 'purple', 'grey', 'white']
        self.root.mainloop()

    def dessineResistance(self):
        """Canevas avec un modèle de résistance à trois lignes colorées"""
        self.size_factor = 3
        self.can = Canvas(self.root, width=250*self.size_factor,height=100*self.size_factor, bg='light blue')
        self.can.grid(row=1, column=1, columnspan=3, pady=5, padx=5)
        self.can.create_line(10*self.size_factor, 50*self.size_factor, 240*self.size_factor, 50*self.size_factor, width=3*self.size_factor)	       # fils
        self.can.create_rectangle(65*self.size_factor, 30*self.size_factor, 185*self.size_factor, 70*self.size_factor, fill='beige', width=2*self.size_factor)
        # Dessin des trois lignes colorées (noires au départ) :
        self.ligne = []         # on mémorisera les trois lignes dans 1 liste
        for x in range(85*self.size_factor, 150*self.size_factor, 24*self.size_factor):
            self.ligne.append(self.can.create_rectangle(x, 31*self.size_factor, x+16*self.size_factor, 69*self.size_factor,
                                                        fill='black', width=0))

    def changeCouleurs(self, *args):
        """Affichage des couleurs correspondant à la valeur entrée"""
        self.v1ch = self.entree.get()	# cette méthode renvoie une chaîne
        try:
            v = float(self.v1ch)        # conversion en valeur numérique
        except:
            err = 1		                # erreur : entrée non numérique
        else:
            err = 0
        if err == 1 or v < 10 or v > 1e11:
            self.signaleErreur()	    # entrée incorrecte ou hors limites
        else:
            self.li = [0]*3 	                # liste des 3 codes à afficher
            logv = int(log10(v))	    # partie entière du logarithme
            ordgr = 10**logv		    # ordre de grandeur
            # extraction du premier chiffre significatif :
            self.li[0] = int(v/ordgr)	    # partie entière
            decim = v/ordgr - self.li[0]	    # partie décimale
            # extraction du second chiffre significatif :
            self.li[1] = int(decim*10 + .5)  # +.5 pour arrondir correctement
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
        self.root.after(1000, self.videEntree)	# après 1 seconde, effacer

    def videEntree(self):
        self.entree.configure(bg='white')       # rétablir le fond blanc
        self.entree.delete(0, len(self.v1ch))
        self.li = [0,0,0]	                    # enlever les car. présents
        self.coloration()                       # réinitialiser les bandes


# Programme principal :
if __name__ == '__main__':
    from tkinter import *
    from math import log10  # logarithmes en base 10
    f = Application()	    # instanciation de l'objet application

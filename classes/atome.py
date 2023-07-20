class Atome:
    """atomes simplifiés, choisis parmi les 10 premiers éléments du TP""" 
    table =[None, ('hydrogène',0),('hélium',2),('lithium',4),
            ('béryllium',5),('bore',6),('carbone',6),('azote',7),
            ('oxygène',8),('fluor',10),('néon',10)]

    def __init__(self, numero_atomique):
        "le n° atomique détermine le n. de protons, d'électrons et de neutrons"
        self.proton, self.electron = numero_atomique, numero_atomique 
        self.neutron = Atome.table[numero_atomique][1]

    def affiche(self):
        print()
        print("Nom de l'élément :", Atome.table[self.proton][0])
        print("%s protons, %s électrons, %s neutrons" % \
            (self.proton, self.electron, self.neutron))

class Ion(Atome):
    """les ions sont des atomes qui ont gagné ou perdu des électrons"""

    def __init__(self, numero_atomique, charge):
        "le n° atomique et la charge électrique déterminent l'ion"
        Atome.__init__(self, numero_atomique)
        self.electron = self.electron - charge
        self.charge = charge

    def affiche(self):
        Atome.affiche(self)
        print("Particule électrisée. Charge =", self.charge)



### Programme principal : ###

a1 = Atome(5)
a2 = Ion(3, 1)
a3 = Ion(8, -2)
a1.affiche()
a2.affiche()
a3.affiche()
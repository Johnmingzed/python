from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk, ImageOps
from rembg import remove

fen = Tk()

image = None  
image_path = None  
dpi_value = DoubleVar(value=100.0)  # Valeur DPI par défaut

# Fonction pour redimensionner l'image
def redimensionner():
    global image
    largeur = int(entr1.get())
    hauteur = int(entr2.get())
    if image:
        image_resized = image.resize((largeur, hauteur))
        image_resized_with_dpi = ImageOps.scale(image_resized, int(dpi_value.get()) / 100)
        photo_resized = ImageTk.PhotoImage(image_resized_with_dpi)
        can1.itemconfig(item, image=photo_resized)
        can1.image = photo_resized  

# Fonction pour supprimer le fond de l'image
def supprimer_fond():
    if image:
        output_path = 'output.png'  # Chemin de l'image de sortie

        input_image = Image.open(image_path)  # Charger l'image d'entrée
        output_image = remove(input_image)  # Supprimer le fond
        output_image.save(output_path)  # Sauvegarder l'image de sortie

        photo_with_alpha = ImageTk.PhotoImage(output_image)
        can1.itemconfig(item, image=photo_with_alpha)
        can1.image = photo_with_alpha  
    else:
        print("Aucune image sélectionnée")

# Fonction pour ouvrir le dialogue de sélection de fichier
def ouvrir_fichier():
    global image, image_path
    filetypes = (("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*"))
    image_path = filedialog.askopenfilename(filetypes=filetypes)
    if image_path:
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        can1.itemconfig(item, image=photo)
        can1.image = photo  

# Fonction pour enregistrer l'image
def enregistrer():
    if image:
        filetypes = (("PNG files", "*.png"), ("All files", "*.*"))
        output_path = filedialog.asksaveasfilename(filetypes=filetypes, defaultextension='.png')
        if output_path:
            image.save(output_path)
            messagebox.showinfo("Enregistrement", "L'image a été enregistrée avec succès.")
    else:
        print("Aucune image à enregistrer.")

# Fonction pour créer une nouvelle image
def nouvelle_image():
    global image, image_path
    image = None
    image_path = None
    can1.itemconfig(item, image='')
    entr1.delete(0, 'end')
    entr2.delete(0, 'end')

# Fonction pour afficher la boîte de dialogue "À propos"
def a_propos():
    messagebox.showinfo("À propos", "Ceci est une application pour redimensionner et supprimer le fond des images.")

# Fonction pour quitter l'application
def quitter():
    fen.quit()

# Création de widgets 'Label' et 'Entry':
txt1 = Label(fen, text='Largeur :')
txt2 = Label(fen, text='Hauteur :')
dpi_label = Label(fen, text='DPI :')
entr1 = Entry(fen)
entr2 = Entry(fen)
dpi_slider = Scale(fen, from_=1, to=100, resolution=1, orient=HORIZONTAL, variable=dpi_value)

# Création d'un widget 'Canvas' contenant une image :
can1 = Canvas(fen, width=800, height=600, bg='white')
item = can1.create_image(400, 300)

#  bouton pour redimensionner l'image
btn_redimensionner = Button(fen, text='Redimensionner', command=redimensionner)

# bouton pour supprimer le fond de l'image
btn_supprimer_fond = Button(fen, text='Supprimer fond', command=supprimer_fond)

# barre de menu
barre_menu = Menu(fen)

# menu "Fichier"
menu_fichier = Menu(barre_menu, tearoff=0)
menu_fichier.add_command(label="Nouveau", command=nouvelle_image)
menu_fichier.add_command(label="Ouvrir", command=ouvrir_fichier)
menu_fichier.add_command(label="Enregistrer", command=enregistrer)
menu_fichier.add_separator()
menu_fichier.add_command(label="Exit", command=quitter)
barre_menu.add_cascade(label="Fichier", menu=menu_fichier)

# menu "Aide"
menu_aide = Menu(barre_menu, tearoff=0)
menu_aide.add_command(label="À propos", command=a_propos)
barre_menu.add_cascade(label="Aide", menu=menu_aide)

# Configuration de la barre de menu
fen.config(menu=barre_menu)

# Mise en page à l'aide de la méthode 'grid' :
txt1.grid(row=1, sticky=E)
txt2.grid(row=2, sticky=E)
dpi_label.grid(row=3, sticky=E)
entr1.grid(row=1, column=2)
entr2.grid(row=2, column=2)
dpi_slider.grid(row=3, column=2, sticky=W+E)
can1.grid(row=1, column=3, rowspan=3, padx=10, pady=5)
btn_redimensionner.grid(row=4, column=2)
btn_supprimer_fond.grid(row=4, column=3)

fen.mainloop()

from tkinter import *
from PIL import Image, ImageTk
from rembg import remove
import rembg
import os

# Path to filesystem definitions
main_dir = os.path.split(os.path.abspath(__file__))[0]


def loadImage(name):
    fullname = os.path.join(main_dir, name)
    return fullname


def findRatio(size):
    return size[0] / size[1]

def removeBg():
    global img
    img = remove(img)


# Preview size
WIDTH = 400
HEIGHT = 400

# Init main Window
root = Tk()
root.configure(width=1280, height=720)
root.title = "Super Gimp 3000"

# Largeur
inputLargeurLabel = Label(root, text="Largeur")
inputLargeur = Entry(root)

# Hauteur
inputHauteurLabel = Label(root, text="Hauteur")
inputHauteur = Entry(root)

# DPI
inputDpiLabel = Label(root, text="DPI")
inputDpi = Entry(root)


# RemoveBG
removeButton = Button(root, text="Remove Background", command=removeBg)


# Image
img = Image.open(loadImage('jonathan.jpg'))
ratio = findRatio(img.size)
factor = img.width // WIDTH if ratio >= 1 else img.height // HEIGHT
img = img.reduce(factor)
imgTk = ImageTk.PhotoImage(img)

# Canvas
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='#112233')
canvas.create_image(WIDTH/2, HEIGHT/2, image=imgTk)

# Disaplay layout
inputHauteurLabel.grid(row=1, sticky=E)
inputLargeurLabel.grid(row=2, sticky=E)
inputDpiLabel.grid(row=3, sticky=E)
removeButton.grid(row=4, sticky=E)
inputHauteur.grid(row=1, column=2)
inputLargeur.grid(row=2, column=2)
inputDpi.grid(row=3, column=2)
canvas.grid(row=1, column=3, rowspan=4)


root.mainloop()

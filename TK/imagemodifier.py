from tkinter import *
from PIL import Image, ImageTk
from rembg import remove
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

    newImg = remove(img)
    displayImage(newImg)

    print('fin du traitement')


def displayImage(img):
    global imgTk, canvas

    imgTk = ImageTk.PhotoImage(img)

    canvas.delete('all')
    canvas.create_image(WIDTH/2, HEIGHT/2, image=imgTk)
    canvas.update()


# Preview size
WIDTH = 720
HEIGHT = 720

# Init main Window
root = Tk()
root.configure(width=1280, height=720)
root.title("Super Gimp 3000")
img = Image.open(loadImage('jonathan.jpg'))

# Canvas
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='#112233')

# Largeur Field
inputLargeurLabel = Label(root, text="Largeur")
imgWidth = img.width if 'img' in globals() else ""
inputLargeur = Entry(root, width=10)
inputLargeur.insert(0, imgWidth)
inputLargeur.update()

# Hauteur Field
inputHauteurLabel = Label(root, text="Hauteur")
imgHeight = img.height if 'img' in globals() else ""
inputHauteur = Entry(root, width=10)
inputHauteur.insert(0, imgHeight)
inputHauteur.update()

# DPI Field
inputDpiLabel = Label(root, text="DPI")
imgDpi = img.info['dpi'][0] if 'img' in globals() else ""
inputDpi = Entry(root, width=10)
inputDpi.insert(0, imgDpi)
inputDpi.update()

# RemoveBG Button
removeButton = Button(root, text="Remove Background", command=removeBg)

# Image
ratio = findRatio(img.size)
factor = img.width // WIDTH if ratio >= 1 else img.height // HEIGHT
img = img.reduce(factor)
displayImage(img)

# Disaplay layout
inputLargeurLabel.grid(row=1, padx=10, stick=E)
inputHauteurLabel.grid(row=2, padx=10, stick=E)
inputDpiLabel.grid(row=3, padx=10, stick=E)
removeButton.grid(row=4, column=1, columnspan=2, padx=10)
inputLargeur.grid(row=1, column=2, sticky=W)
inputHauteur.grid(row=2, column=2, sticky=W)
inputDpi.grid(row=3, column=2, sticky=W)
canvas.grid(row=1, column=3, rowspan=4)


root.mainloop()

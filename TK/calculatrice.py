from tkinter import *
from math import *


def compute(event):
    result = str(eval(inputWidget.get()))
    resultWidget.configure(text=result)


def follow(event):
    mousePositionX = event.x
    mousePositionY = event.y
    mousePosition = "Position : " + \
        str(mousePositionX) + " | " + str(mousePositionY)
    position.configure(text=mousePosition)


root = Tk()
root.title('Super Calculatrice 3000')
root.configure(background='#112233')

position = Label(root, text="Position de la souris", padx=10, pady=10, font=(
    'Arial', 16, 'bold'), background='#112233', foreground='#FFA200')
position.pack(side=TOP)

inputWidget = Entry(root, width=40, justify=CENTER, font=(
    'Arial', 16, 'bold'), background='#445566', foreground='#FFA200')
inputWidget.bind("<Return>", compute)
inputWidget.bind("<Motion>", follow)
inputWidget.pack(padx=20, pady=20)

result = "Veuillez entrer votre calcul"
resultWidget = Label(root, text=result, padx=10, pady=10, font=(
    'Arial', 16, 'bold'), background='#112233', foreground='#FFA200')
resultWidget.pack(side=BOTTOM)

root.mainloop()

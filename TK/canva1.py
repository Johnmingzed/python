from tkinter import *
import random


def randHex():
    # Create a 2-digit hex string based on a radom int
    hexa = hex(random.randint(0, 255))[2:]
    # Fill with leading zero if needed
    return hexa.zfill(2)


class Line(object):

    def __init__(self):
        self.x1, self.y2 = 0, 0
        self.y1, self.x2 = 400, 400
        self.color = '#FFFFFF'

    def trace(self):
        self.y1 = random.randint(0, 400)
        self.y2 = random.randint(0, 400)
        canvas.create_line(self.x1, self.y1, self.x2, self.y2,
            fill=self.color, smooth=True, width=random.randint(0, 10))

    def changeColor(self):
        self.color = '#' + randHex() + randHex() + randHex()

    def total(self):
        self.changeColor()
        self.trace()


# Main window init
root = Tk()

# Layout init
canvas = Canvas(root, width=400, height=400, background='#112233')
canvas.pack(side=LEFT)

# Line drawer object init
line = Line()

# Button to trace line
traceLineButton = Button(root, text="Tracer une ligne", command=line.trace)
traceLineButton.pack(side=TOP)  # Rendering

# Button to change color
changeColorButton = Button(
    root, text="Changer de couleur", command=line.changeColor)
changeColorButton.pack(side=TOP)  # Rendering

# Button to quit
quitButton = Button(root, text="Quitter", command=root.destroy)
quitButton.pack(side=BOTTOM)  # Rendering

# Button to trace a random line
randomButton = Button(root, text="Random", command=line.total)
randomButton.pack(side=TOP)  # Rendering

# Render windows
root.mainloop()

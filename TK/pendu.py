from tkinter import *


class Pendu(object):
    def __init__(self):
        self.pattern = [
            ('line', 20, 380, 380, 380),
            ('line', 120, 380, 120, 20),
            ('line', 120, 20, 300, 20),
            ('line', 120, 60, 160, 20),
            ('line', 250, 20, 250, 100),
            ('oval', 230, 100, 270, 140),
            ('line', 250, 140, 250, 240),
            ('line', 250, 240, 220, 320),
            ('line', 250, 240, 280, 320),
            ('line', 250, 160, 220, 220),
            ('line', 250, 160, 280, 220)
        ]
        self.cursor = 0
        self.color = '#FFA200'
        self.width = 5


def draw():
    step = pendu.cursor
    if step <= len(pendu.pattern) - 1:
        drawPendu = pendu.pattern[step]
        playButton.configure(text='Jouer')
        if drawPendu[0] == 'line':
            canva.create_line(drawPendu[1], drawPendu[2], drawPendu[3],
                drawPendu[4], fill=pendu.color, width=pendu.width)
        elif drawPendu[0] == 'oval':
            canva.create_oval(drawPendu[1], drawPendu[2], drawPendu[3],
                drawPendu[4], outline=pendu.color, width=pendu.width)
        pendu.cursor += 1
    else:
        pendu.cursor = 0
        playButton.configure(text='Rejouer')
        canva.delete('all')


root = Tk()
root.title("Super Pendu 3000")
pendu = Pendu()

canva = Canvas(root, background='#112233', height=400, width=400)
canva.pack(side=TOP)

playButton = Button(root, text="Jouer", command=draw)
playButton.pack(side=BOTTOM)

root.mainloop()

from tkinter import *

def select(*args):
    sel = "Value = " + str(v.get())
    T.configure(width=3*v.get(), height=v.get())

root = Tk()
root.geometry("700x500")
v = IntVar()
scale = Scale(root, variable=v, from_=1, to=50, orient=HORIZONTAL)

# Lier l'événement "<Configure>" à la fonction select
#scale.bind("<Configure>", select)
v.trace_add("write", select)

scale.pack(anchor=CENTER)

T = Text(root)
T.configure(width=10, height=5)
T.pack()

root.mainloop()

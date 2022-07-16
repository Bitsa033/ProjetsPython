import os
from tkinter import *

# Largeur de la fenetre
Largeur = 400
# Hauteur de la fenetre
Hauteur = 400
# on cree la fenetre
window = Tk()
# on configure les dimensions de la fenetre
canvas = Canvas(width=Largeur, height=Hauteur, background='white')
canvas.pack(fill="both", expand="true")
xo, yo = 100, 100
dx = +5
dy = +2
rect = canvas.create_rectangle(xo, yo, xo + 20, yo + 20, width=2, fill="red")


def deplacer():
    global xo, yo, dx, dy
    xo = xo + dx
    yo = yo + dy
    canvas.coords(rect, xo, yo, xo + 20, yo + 20)

    if xo < 0 or xo > Hauteur:
        dx = -dx
    elif yo < 0 or yo > Largeur:
        dy = -dy
    canvas.after(50, deplacer)

    return


def action_deplacer():
    deplacer()
    return


button = Button(text="lancer", command=action_deplacer)
button.pack()

window.mainloop()

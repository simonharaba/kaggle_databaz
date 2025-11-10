import tkinter
canvas=tkinter.Canvas()
from random import *
canvas.pack()
farba=choice['red','blue','green','yellow']

def slovo:
    canvas.create_text(100,100, text=entry1, fill=farba)
entry1=tkinter.Entry()
entry1.pack()
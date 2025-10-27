import tkinter
from random import *
canvas=tkinter.Canvas()
canvas.pack()

def run():
    slovo=entry1.get()
    x=20
    for ktore in range(len(slovo)):
        canvas.create_text(x,100, text=slovo[ktore], fill=choice(('red','blue','green','yellow')))
        x+=30

entry1=tkinter.Entry()
entry1.pack()

button1=tkinter.Button(text='ok', command=run)
button1.pack()

canvas.mainloop()
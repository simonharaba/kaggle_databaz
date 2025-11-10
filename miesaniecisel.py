import tkinter
from random import *
canvas=tkinter.Canvas()
canvas.pack()

novecislo=''
def random():
    global novecislo
    
    for cislo in cisla():
        novecislo=randint(1,16)




    cislo = []
    cisla = [novecislo] * 3
    for i in range(5):
        
        cislo.append(cisla)
        print(cisla)
random()


canvas.mainloop()
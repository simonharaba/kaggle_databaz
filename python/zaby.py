import tkinter
from random import *
canvas = tkinter.Canvas(width=610, height=270, bg='white')
canvas.pack()

obrazok=tkinter.PhotoImage(file='zaba1.png')
sirka_zaby = 60
zaby = list(range(10))
print(zaby)
for i in range(len(zaby)):
    ktory = randrange(10)
    zaby[i], zaby[ktory] = zaby[ktory], zaby[i]
print(zaby)

def kresli_zabu(x, y, cislo):
    
    canvas.create_line(x, y+55, x+55, y+55, width=3, fill='green')
    if cislo != 0:
        
        canvas.create_image(x+50,y,image=obrazok)
        canvas.create_text(x+48, y-50, text=cislo)
def kresli():
    canvas.delete('all')
    for i in range(len(zaby)):
        kresli_zabu(i*sirka_zaby, 100, zaby[i])
kresli()
posun=0
def klik(sur):
    global posun
    index = (sur.x - 10)//sirka_zaby
    prazdne = zaby.index(0)
    vzdialenost = abs(index-prazdne)
    if vzdialenost < 3 and 0 <= index <= 9:
        zaby[index], zaby[prazdne] = zaby[prazdne], zaby[index]
        posun+=1
        kresli()
        print(posun)
        if vyherna_pozicia():
            gratulacia()
canvas.bind('<Button-1>', klik)

def vyherna_pozicia():
    for i in range(len(zaby)-1):
        if i != zaby[i]-1:
            return False
    return True
def gratulacia():
    canvas.create_text(300, 200, text='Vyhral si!', font='Arial 50', fill='green')
canvas.mainloop()
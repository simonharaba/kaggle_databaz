import tkinter
from random import * 
canvas=tkinter.Canvas()
canvas.pack()


taniere=['A','B','C','D','E','F','G','H','I','J']
pocetx=[]
pocety=[]
x=20
y=100
i=0
surx=0
sury=0

for tanier in taniere:
        canvas.create_oval(x,y,x+20,y+20,fill='blue')
        canvas.create_text(x+10,y+10,text=taniere[i],font=('Arial',10),fill='white')
        x+=30
        i+=1

def klik(event):
    global x,y,surx,sury
    surx=event.x
    sury=event.y
def pozicia():
    global x,y,surx,sury,taniere
    
    if x<surx<x+20 and 100<y<120:
        pocetx.append(taniere)
        print(pocetx)

vybraty=randint(1,10)
canvas.create_oval(0+20*vybraty,120,20+20*vybraty,140,fill='red',tags='prasknuty')
    

pozicia()



canvas.bind('<Button-1>',klik)

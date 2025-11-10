
import tkinter
from random import*
canvas = tkinter.Canvas(width=600, height=150, bg='white')
canvas.pack()

ziadny=-10
sirka=30

def select():
    global selected
    for j in range(20):
        vzdial=abs(selected-j)
        if vzdial==0:
            zoom=3
        elif vzdial==1:
            zoom=2
        else:
            zoom=1
        vyska=sirka*zoom
        canvas.delete(stvorcek[j])
        stvorcek[j]=canvas.create_rectangle(j*sirka,60-vyska/2,(j+1)*sirka,60+vyska/2,fill=farby[j])

def pohyb(event):
    global selected
    if 60-sirka/2<event.y<60+sirka/2:
        j=event.x // sirka
        if j<0 or j>=20:
            j=ziadny
    else:
        j=ziadny
    if j!=selected:
        selected=j
        select()

stvorcek=[]
farby=[]
for i in range(20):
    farby.append(choice(['yellow','red','green','blue','cyan','magenta']))
    stvorcek.append(canvas.create_rectangle(i*sirka,60-sirka/2,(i+1)*sirka,60+sirka/2,fill=farby[-1]))

selected=ziadny


canvas.bind('<Motion>', pohyb)
canvas.mainloop()
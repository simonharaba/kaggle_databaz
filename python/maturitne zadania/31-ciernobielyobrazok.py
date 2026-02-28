import tkinter
def bod(x,y,farba):
    canvas.create_rectangle(x,y,x+1,y+1,width=0,fill=farba)
def vykresli(vsetky_odtiene):
    canvas.delete('all')
    subor=open(nazov,'r')
    riadok=subor.readline()
    y=0
    for riadok in subor:
        riadok=riadok.strip()
        x=0
        for i in range(sirka):
            odtien=riadok[i*2:i*2+2]
            if not vsetky_odtiene:
                farba='black'
                if odtien>'7f':
                    farba='white'
            else:
                farba='#'+3*odtien
            bod(x,y,farba)
            x+=1
        canvas.update()
        y=y+1
    subor.close()
def cb():
    vykresli(False)
nazov='31-ciernobielyobrazok.txt'
subor=open(nazov,'r')
riadok=subor.readline()
subor.close()
velkost=riadok.split()
sirka=int(velkost[0])
vyska=int(velkost[1])
canvas=tkinter.Canvas(width=sirka,height=vyska,bg='white')
canvas.pack()

button1=tkinter.Button(text='len cierna a biela',command=cb)
button1.pack()

vykresli(True)

canvas.mainloop()

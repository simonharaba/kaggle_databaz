import tkinter
canvas=tkinter.Canvas(width=400,height=400)
canvas.pack()


def posun():
    global xhlava,yhlava,narazil
    xhlava+=sx
    yhlava+=sy
    z=canvas.coords('hada')
    zx=z[::2]
    zy=z[1::2]
    i=0
    while i<len(zx) and not narazil:
        if zx[i]==xhlava and zy[i]==yhlava:
            narazil=True
        i+=1
    if not narazil:
        z.append(xhlava)
        z.append(yhlava)
        canvas.coords('hada',z)
        canvas.after(2,posun)
def klaves(event):
    global sx,sy
    if event.keysym=='Left':
        sx,sy=-1,0
    if event.keysym=='Right':
        sx,sy=1,0
    if event.keysym=='Up':
        sx,sy=-0,-1
    if event.keysym=='Down':
        sx,sy=-0,1
        
narazil=False
xhlava,yhlava=200,200
sx,sy=0,-1
canvas.create_line(xhlava,yhlava-sy,xhlava,yhlava,tags='hada')
posun()
canvas.bind_all('<Key>',klaves)

canvas.mainloop()
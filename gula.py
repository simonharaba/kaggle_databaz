import tkinter
canvas=tkinter.Canvas(width=400,height=400)
canvas.pack()

pocet=0
def gula(suradnice):
    global pocet
    x=suradnice.x
    y=suradnice.y
    if pocet<100:
        canvas.create_oval(x,y,x+10,y+10,fill='red',tags='lopta')
        pocet+=1
    while y<400:
        y+=10
        canvas.move('lopta',0,5)
        canvas.update()
        canvas.after(10)
        
    else:
        y-=400
        canvas.move('lopta',0,-400)
        canvas.update()
        canvas.after(10)
        gula(suradnice)


canvas.bind('<Button-1>', gula)

canvas.mainloop()
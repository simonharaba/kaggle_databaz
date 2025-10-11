import tkinter
import random
canvas=tkinter.Canvas(bg='black')
canvas.pack()
cisla=('31','62','125','250','500','1K','2K','4K','8K','16K','[HZ]')

x = 20
y = 200
def vyska():
    x = 20
    y = 200
    canvas.delete('vysky')
    for i in range(1, 11):
        s = random.randint(1, 20)
        canvas.create_rectangle(x, y, x + 20, y - 5 * s, fill='green', tags='vysky')
        x += 25
    canvas.update()
    canvas.after(1000, vyska)
vyska()
def ntica():
    global x,y
    for cislo in cisla:
        canvas.create_text(x+10,y+20,text=cislo,fill='green')
        x+=25
    
ntica()

canvas.mainloop()

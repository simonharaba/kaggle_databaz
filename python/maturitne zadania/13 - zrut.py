#13 zrut

import tkinter 
import random
canvas = tkinter.Canvas(width=500, height=500, bg = "white") 
canvas.pack() 
polomer = 25 
jablka = []

for i in range (5): 
    x= random.randint(0, 450) 
    y = random.randint(0, 450) 
    jablko_umiest = canvas.create_oval(x-polomer, y - polomer , x+ polomer, y + polomer, fill="red") 
    jablka.append((x,y, jablko_umiest))

py, px = 50, 50 
sx, sy =1, 0 

zrut_prisera = canvas.create_oval(50-polomer, 50-polomer,50+polomer,50+polomer, fill="blue") 

def zrut(event): 
    global sx, sy 
    if event.keysym == "w": 
        sx, sy = 0, -1 
    elif event.keysym == "s": 
        sx, sy =0, 1 
    elif event.keysym == "a": 
        sx, sy = -1, 0 
    elif event.keysym == "d": 
        sx, sy = 1, 0
            
def animuj():            
    global px, py, jablka
    canvas.move(zrut_prisera, sx, sy)
    px += sx
    py += sy
    print("x: ", px, "y: ",py )
    nove_jablka = []
    for (x,y,jablko_umiest ) in jablka:
        if (x - polomer <= px <= x + polomer) and (y - polomer <= py <= y + polomer):
            canvas.delete(jablko_umiest)
        else:
            nove_jablka.append((x,y,jablko_umiest)) 
    jablka = nove_jablka 
    # ak uz nezostali ziadne jablka, vypis gratulaciu
    if len(jablka) == 0:
        canvas.create_text(250, 250, text="Vyhral si!", font=("Arial", 24), fill="green")
        return
    canvas.after(1, animuj)


canvas.bind_all("<Key>", zrut)
animuj() 
print(jablka) 
canvas.mainloop()

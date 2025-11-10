import tkinter
canvas = tkinter.Canvas(width=1200, height=500,bg='blue')
canvas.pack()

subor = open('x.txt', 'r')
cislox = [int(riadok.strip()) for riadok in subor]

subor2 = open('y.txt', 'r')
cisloy = [int(riadok.strip()) for riadok in subor2]

index = 0

def kresli():
    global index
    if index < len(cislox):
        x = cislox[index]
        y = cisloy[index]
        canvas.create_oval(x-5, y-5, x+5, y+5, fill='white')
        index += 1
        
        canvas.after(1, kresli)

kresli()
canvas.mainloop()

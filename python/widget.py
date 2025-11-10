import tkinter
canvas = tkinter.Canvas(width=440, height=200, bg='white')
canvas.pack()
rx, ry = 100, 50
x, y = 200, 100
canvas.create_oval(x-rx, y-ry, x+rx, y+ry, width=5, outline='green',tags='oval')
def zmena1(event):
    global rx
    rx = scale1.get()
    prekresli()
def zmena2(event):
    global ry
    ry = scale2.get()
    prekresli()
def prekresli():
    canvas.coords('oval',[x-rx, y-ry, x+rx, y+ry])
scale1 = tkinter.Scale(from_=-200, to=200, orient='horizontal',length=400, command=zmena1)
scale1.pack()
scale1.set(rx)
scale2 = tkinter.Scale(from_=-100, to=100, orient='vertical',length=200, command=zmena2)
scale2.place(x=400, y=0)
scale2.set(ry)
canvas.mainloop()

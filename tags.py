import tkinter
canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()
canvas.create_rectangle(100, 100, 180, 180, fill='blue',tags=('obdlznik', 'farba1'))
canvas.create_rectangle(200, 100, 280, 180, fill='red',tags=('obdlznik', 'farba2'))
canvas.create_oval(100, 200, 180, 280, fill='blue', tags=('kruh', 'farba1'))
canvas.create_oval(200, 200, 280, 280, fill='red', tags=('kruh', 'farba2'))

canvas.itemconfig('farba1',fill='green')

canvas.mainloop()   
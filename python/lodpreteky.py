#lodpreteky
import tkinter
canvas = tkinter.Canvas(width=400, height=1000)
from random import *
canvas.pack()

pozicie_y = [60 + i*45 for i in range(15)]
boats = []
winner = None

def lod(x, y, tag):
    canvas.create_rectangle(x, y, x+20, y+10, tags=tag)
    canvas.create_line(x+5, y, x+5, y-15, tags=tag)
    canvas.create_line(x+5, y-15, x+randrange(10,20), y-5, x+5, y-3, tags=tag)

for i in range(15):
    y_pos = pozicie_y[i]
    tag = f'lodka{i}'
    boats.append({'x': 0, 'y': y_pos, 'tag': tag, 'skocil': False, 'index': i+1})
    lod(10, y_pos, tag)

def pohyb():
    global winner
    all_finished = True
    for boat in boats:
        if not boat['skocil']:
            all_finished = False
            speed = randrange(5, 10)
            boat['x'] += speed
            canvas.move(boat['tag'], speed, 0)
            if boat['x'] >= 350:
                
                canvas.move(boat['tag'], -speed, 0)
                boat['skoncil'] = True
                if winner is None:
                    winner = boat['index']
                    canvas.create_text(200, 250, text=f'vitaz{winner}', font=('Arial', 20))
    if not all_finished:
        canvas.after(50, pohyb)

pohyb()

def add_boat():
    y = choice(pozicie_y)
    tag = f'lodka{len(boats)}'
    boats.append({'x': 10, 'y': y, 'tag': tag, 'skoncil': False})
    lod(10, y, tag)

canvas.bind('<Button-1>', lambda event: add_boat())

canvas.mainloop()

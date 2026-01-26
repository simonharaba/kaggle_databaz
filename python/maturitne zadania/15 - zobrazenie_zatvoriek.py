#15 zatvorky

import tkinter

canvas = tkinter.Canvas(width=1000, height=120, bg='white')
canvas.pack()
vyraz = input('Zadajte výraz: ')
pocet = 0
ok = True

for znak in vyraz:
    if znak == '(':
        pocet += 1
    elif znak == ')':
        pocet -= 1
        if pocet < 0:
            ok = False
            break

if ok and pocet != 0:
    ok = False

farby = ['blue', 'fuchsia', 'green', 'maroon', 'purple', 'red','yellow']

if ok:
    oznam = 'Uzátvorkovanie je správne'
else:
    oznam = 'Uzátvorkovanie je nesprávne'

canvas.create_text(500, 90, text=oznam, font='Courier 30')

if ok:
    ktora = -1
    x = 3
    for znak in vyraz:
        if znak == '(':
            ktora += 1
        if znak == '(' or znak == ')':
            canvas.create_text(x, 5, anchor='nw', text=znak, font='Courier 30', fill=farby[ktora])
        else:
            canvas.create_text(x, 5, anchor='nw', text=znak, font='Courier 30', fill='black')
        if znak == ')':
            ktora -= 1
        x += 30

canvas.mainloop()

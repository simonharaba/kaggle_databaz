#zastavky
import tkinter
canvas = tkinter.Canvas(width=220, height=50, background='black')
canvas.pack()

def animacia():
    global nazov
    nazov = nazov[1:] + nazov[0]
    canvas.delete('all')
    canvas.create_text(110,25, text = nazov, fill = 'red', font= 'Arial 20')
    canvas.after(100, animacia)

def vypis(index, zastavky, konecna):
    global nazov
    nazov = zastavky[index] + ' '
    if konecna:
        nazov += ' - konecna zastavka, vystupovat '
    nazov = nazov + ' '*(20-len(nazov))

def dalsie(event):
    global aktualna, konecna
    if not konecna:
        aktualna += 1
        if aktualna == len(zastavky)-1:
            konecna = True
        vypis(aktualna, zastavky, konecna)

subor = open('zastavky.txt', 'r')

zastavky = []
for zastavka in subor:
    zastavky.append(zastavka.strip())
aktualna = 0
konecna = False
nazov = ''
vypis(aktualna, zastavky, konecna)
animacia()

print(zastavky)

subor.close()
canvas.bind_all('<Key>', dalsie)

canvas.mainloop()

""" import tkinter
canvas = tkinter.Canvas(width=220, height=50, background='red')
canvas.pack()

subor = open('zastavky.txt', 'r')

for zastavka in subor:
    while True:


def klik(event):


canvas.bind_all('<Key>', klik)

subor.close()

canvas.mainloop() """
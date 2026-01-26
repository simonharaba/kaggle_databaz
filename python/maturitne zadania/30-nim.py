import tkinter

canvas = tkinter.Canvas(width=650, height=200)
canvas.pack()

pocet_zapaliek = 15

def zapalka(x, y):
    canvas.create_line(x, y, x, y+100, width=5, fill='yellow')
    canvas.create_oval(x-5, y-5, x+5, y+8, fill='brown', outline='brown')

def prekresli():
    canvas.delete('all')
    for i in range(pocet_zapaliek):
        zapalka(30 + i*40, 50)
    canvas.create_text(325, 180, text="Zostáva zápaliek: " + str(pocet_zapaliek), font="Arial 16")
    
    if pocet_zapaliek == 0:
        canvas.create_text(325, 100, text="VYHRAL SI! GRATULUJEM!", fill="red", font="Arial 25")

def tah(event):
    global pocet_zapaliek
    if pocet_zapaliek > 0:
        try: # Použité len na prevod znaku, ak by niekto stlačil niečo iné
            pocet = int(event.char)
            if pocet in [1, 2, 3]:
                if pocet_zapaliek >= pocet:
                    pocet_zapaliek -= pocet
                    prekresli()
        except:
            pass

prekresli()

# Reagovanie na klávesy
canvas.bind_all('1', tah)
canvas.bind_all('2', tah)
canvas.bind_all('3', tah)

tkinter.mainloop()
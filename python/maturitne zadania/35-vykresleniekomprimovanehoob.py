import tkinter

def vykresli(negativ=False):
    canvas.delete('all')
    f = open('34-vstup.txt', 'r')
    riadok1 = f.readline().split()
    sirka, vyska = int(riadok1[0]), int(riadok1[1])
    
    y = 0
    for riadok in f:
        cisla = riadok.split()
        x = 0
        farba_index = 0 # 0 pre čiernu, 1 pre bielu
        for pocet in cisla:
            pocet = int(pocet)
            # Logika farby: ak je negatív, otočíme význam indexu
            aktualna_farba = 'white' if (farba_index == 1 if not negativ else farba_index == 0) else 'black'
            
            if aktualna_farba == 'black':
                canvas.create_line(x, y, x + pocet, y, fill='black')
            
            x += pocet
            farba_index = 1 - farba_index # striedanie 0 a 1
        y += 1
    f.close()

f_rozmery = open('34-vstup.txt', 'r')
r1 = f_rozmery.readline().split()
s, v = int(r1[0]), int(r1[1])
f_rozmery.close()

canvas = tkinter.Canvas(width=s, height=v, bg='white')
canvas.pack()

btn_negativ = tkinter.Button(text='Negatív', command=lambda: vykresli(negativ=True))
btn_negativ.pack()

vykresli() # Prvotné vykreslenie
tkinter.mainloop()
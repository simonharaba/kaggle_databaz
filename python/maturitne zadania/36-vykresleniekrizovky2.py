import tkinter

def kresli_krizovku(x_start, y_start, velkost, vyplnena=True):
    f = open('36-krizovka.txt', 'r')
    tajnicka = f.readline().strip().upper()
    slova = [line.strip().upper() for line in f]
    f.close()

    for i in range(len(slova)):
        slovo = slova[i]
        pismeno_t = tajnicka[i]
        pozicia = slovo.find(pismeno_t)
        
        # Výpočet začiatku riadku tak, aby tajnička bola na x_start
        riadok_x = x_start - (pozicia * velkost)
        riadok_y = y_start + (i * velkost)
        
        for j in range(len(slovo)):
            x = riadok_x + (j * velkost)
            farba = 'grey' if j == pozicia else 'white'
            canvas.create_rectangle(x, riadok_y, x + velkost, riadok_y + velkost, fill=farba)
            if vyplnena:
                canvas.create_text(x + velkost/2, riadok_y + velkost/2, text=slovo[j])

canvas = tkinter.Canvas(width=800, height=500)
canvas.pack()

kresli_krizovku(150, 50, 30, vyplnena=False) # Nevyplnená vľavo
kresli_krizovku(450, 50, 30, vyplnena=True)  # Vyplnená vpravo

tkinter.mainloop()
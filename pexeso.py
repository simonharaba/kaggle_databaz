import tkinter, random
canvas = tkinter.Canvas(width=800, height=400)
canvas.pack()
def nacitaj(nazov, typ, pocet, obrazky):
    for i in range(1, pocet+1):
        obrazok = tkinter.PhotoImage(file=nazov + str(i) + '.'+typ)
        obrazky.append(obrazok)
def kresli_rub(x, y, oznacenia):
    poradie = 0
    for j in range (4):
        for i in range(8):
            canvas.create_image(x + i*90, y + j*90, image=pexeso,tags=oznacenia[poradie])
            poradie += 1
obrazky = []
nacitaj('pvp2-subory/obrazky/oz_', 'png', 16, obrazky)
pexeso = tkinter.PhotoImage(file='pvp2-subory/obrazky/pexeso.png')
oznacenia = []
for i in range(16):
    oznacenia.append('rub_'+str(i))
oznacenia = oznacenia + oznacenia
random.shuffle(oznacenia)
kresli_rub(50, 50, oznacenia)


def klik(event):
    zakliknute = canvas.find_withtag('current')
    if len(zakliknute) > 0:
        zakliknuty = zakliknute[0]
        tagy = canvas.gettags(zakliknuty)
        if tagy[0] != 'current':
            stara_znacka = tagy[0]
        else:    
            stara_znacka = tagy[1]
        info = stara_znacka.split('_')
        if info[0] == 'rub':
            nova_znacka = 'lice_'+info[1]
            cislo_obrazku = int(info[1])
            canvas.addtag(nova_znacka, 'withtag', zakliknuty)
            canvas.dtag(zakliknuty, stara_znacka)
            canvas.itemconfig(zakliknuty, image=obrazky[cislo_obrazku])
        if info[0] == 'lice':
            nova_znacka = 'rub_'+info[1]
            canvas.addtag(nova_znacka, 'withtag', zakliknuty)
            canvas.dtag(zakliknuty, stara_znacka)
            canvas.itemconfig(zakliknuty, image=pexeso)
canvas.bind('<Button-1>', klik)


canvas.mainloop()
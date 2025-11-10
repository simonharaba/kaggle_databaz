# p1-02.py
import tkinter
canvas = tkinter.Canvas(width=700, height=600, bg='black')
canvas.pack()

obrazky_nazvy = ('prazdne', 'diamant', 'dvereotv', 'stena', 'voda', 'dvere', 'figurka')
obrazky = []
plocha = []

def nacitaj_obrazky():
    for nazov in obrazky_nazvy:
        obrazok = tkinter.PhotoImage(file='diamanty/'+nazov+'.png')
        obrazky.append(obrazok)

def nacitaj_plochu():
    subor = open('diamanty/data2.txt')
    for riadok in subor:
        riadok = riadok[::2]
        riadok_cisla = []
        for znak in riadok:
            riadok_cisla.append(int(znak))
        plocha.append(riadok_cisla)
    subor.close()

def kresli_obrazok(x, y, cislo):
    canvas.create_image(x, y, image=obrazky[cislo], anchor='nw')
    
def vykresli_plochu():
    for r in range(10):
        for s in range(10):
            kresli_obrazok(s*70, r*60, plocha[r][s])
    
nacitaj_obrazky()
nacitaj_plochu()
vykresli_plochu()

def najdi_policko(typ_policka):
    for r in range(10):
        for s in range(10):
            if plocha[r][s] == typ_policka:
                return s, r
hrac = najdi_policko(6)

def spocitaj_diamanty():
    
    pocet = 0
    for r in range(10):
        for s in range(10):
            if plocha[r][s] == 1:
                pocet += 1
                
    return pocet
pocet_diamantov = spocitaj_diamanty()


def klaves(event):
    global smer
    smer = (0, 0)
    if event.keysym == 'Left':
        smer = (-1, 0)
    if event.keysym == 'Right':
        smer = (1, 0)
    if event.keysym == 'Up':
        smer = (0, -1)
    if event.keysym == 'Down':
        smer = (0, 1)
    if smer != (0, 0):
        skus_posun()
smer = (0, 0)
canvas.bind_all('<Key>', klaves)

def skus_posun():
    nove_x = hrac[0] + smer[0]
    nove_y = hrac[1] + smer[1]
    if 0 <= nove_x <= 9 and 0 <= nove_y <= 9:
        if plocha[nove_y][nove_x] < 3:
            posun_sa(nove_x, nove_y, plocha[nove_y][nove_x])

def posun_sa(nove_x, nove_y, typ_policka):
    global hrac, pocet_diamantov
    plocha[hrac[1]][hrac[0]] = 0
    hrac = (nove_x, nove_y)
    plocha[hrac[1]][hrac[0]] = 6
    if typ_policka == 1:
        pocet_diamantov -= 1
        if pocet_diamantov == 0:
            otvor_dvere()
    vykresli_plochu()
    if typ_policka == 2:
        dalsi_level()
    canvas.delete('dia')
    canvas.create_text(500,550,text='pocet diamantov je: '+str(pocet_diamantov),fill='red',font=('Arial',20),tags='dia')
    

def otvor_dvere():
    x, y = najdi_policko(5)
    plocha[y][x] = 2


def dalsi_level():
    global pocet_diamantov, plocha, hrac
    plocha = plocha[10:]
    if plocha == []:
        koniec_hry()
    else:
        vykresli_plochu()
        pocet_diamantov = spocitaj_diamanty()
        hrac = najdi_policko(6)
def koniec_hry():
    canvas.unbind_all('<Key>')
    canvas.create_text(350, 300, text='Super! Prešiel si všetko!',font='Arial 20', fill='yellow')


canvas.mainloop()
# p1-01g.py
import tkinter
canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()
pocet_policok_x, pocet_policok_y = 10, 8
v = 30 #veľkost políčka
mriezka_x, mriezka_y = 10, 10      # x a y začiatku mriežky
vypln = 1
plocha = []

for i in range(pocet_policok_y):
    plocha.append([0]*pocet_policok_x)

def kresli_mriezku(px, py, v, mx, my):
    for stlpec in range(px):
        for riadok in range(py):
            canvas.create_rectangle(stlpec*v + mx, riadok*v + my,
                                    (stlpec+1)*v + mx, (riadok+1)*v + my)

def kresli(stlpec, riadok, vypln):
    if vypln == 1:
        canvas.create_oval(stlpec*v + mriezka_x +1, riadok*v+mriezka_y+1,
                           (stlpec+1)*v+mriezka_x -2, (riadok+1)*v+mriezka_y-2,
                           fill = 'red')
    if vypln == 2:
        canvas.create_line(stlpec*v + mriezka_x +1, riadok*v+mriezka_y+1,
                           (stlpec+1)*v+mriezka_x -1, (riadok+1)*v+mriezka_y+1,
                           fill = 'blue', width = 2)
        canvas.create_line(stlpec*v + mriezka_x +1, (riadok+1)*v+mriezka_y+1,
                           (stlpec+1)*v+mriezka_x -1, riadok*v + mriezka_y+1,
                           fill = 'blue', width = 2)

def pozicia(x, y):
    stlpec = (x - mriezka_x) // v
    riadok = (y - mriezka_y) // v
    return stlpec, riadok    
    
def oznac(sur):
    global vypln
    stlpec, riadok = pozicia(sur.x, sur.y)
    if plocha[riadok][stlpec] == 0:
        vypln = 3 - vypln
        plocha[riadok][stlpec] = vypln
        kresli(stlpec, riadok, vypln)

def save():
    subor = open('piskvorky.txt', 'w')
    subor.write(str(pocet_policok_x)+' '+str(pocet_policok_y)+'\n')
    for riadok in plocha:
        zapisat = ''
        for prvok in riadok:
            zapisat = zapisat + str(prvok) + ' '
        zapisat = zapisat[:-1]+'\n'
        subor.write(zapisat)
    subor.close()

def int_zoznam(zoznam):
    vysledok = []
    for prvok in zoznam:
        vysledok.append(int(prvok))
    return vysledok

def kresli_plochu():
    for r in range(pocet_policok_y):
        for s in range(pocet_policok_x):
            kresli(s, r, plocha[r][s])

def load():
    global pocet_policok_x, pocet_policok_y, plocha
    subor = open('piskvorky.txt', 'r')
    info = subor.readline()
    info = info.strip()
    rozmery = info.split()
    pocet_policok_x, pocet_policok_y = int_zoznam(rozmery)
    plocha = []
    for riadok in subor:
        riadok = riadok.strip()
        riadok_zoznam = riadok.split()
        riadok_zoznam = int_zoznam(riadok_zoznam)
        plocha.append(riadok_zoznam)
    canvas.delete('all')
    kresli_mriezku(pocet_policok_x, pocet_policok_y, v, mriezka_x, mriezka_y)
    kresli_plochu()
    
def zmen():
    global plocha, pocet_policok_x, pocet_policok_y
    for i in range(pocet_policok_y):
        for j in range(pocet_policok_x):
            if plocha[i][j] == 1:
                plocha[i][j] = 2
            elif plocha[i][j] == 2:
                plocha[i][j] = 1
    save()
    load()



def prekresli(nova_velkost):
    global v
    v=int(nova_velkost)
    canvas.delete('all')
    kresli_mriezku(pocet_policok_x, pocet_policok_y, v, mriezka_x, mriezka_y)
    kresli_plochu()

def pocet():
    global plocha, pocet_policok_x, pocet_policok_y,jednotky,dvojky
    jednotky=0
    dvojky=0
    for i in range(pocet_policok_y):
        for j in range(pocet_policok_x):
            if plocha[i][j] == 1:
                dvojky+=1
            elif plocha[i][j] == 2:
                jednotky+=1
    print(str(jednotky)+' '+str(dvojky))
    save()
    load()





scale1 = tkinter.Scale(from_=-200, to=200,orient='horizontal',length=400, command=prekresli)
scale1.pack()
scale1.set(v)

button1 = tkinter.Button(text='Save', command=save)
button1.pack()
button2 = tkinter.Button(text='Load', command=load)
button2.pack()
button3 = tkinter.Button(text='Zmen', command=zmen)
button3.pack()
button4 = tkinter.Button(text='rataj', command=pocet)
button4.pack()


kresli_mriezku(pocet_policok_x, pocet_policok_y, v, mriezka_x, mriezka_y)

canvas.bind('<Button-1>', oznac)

canvas.mainloop()
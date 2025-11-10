import tkinter
canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()
pocet_policok_x, pocet_policok_y = 10, 8
v = 30 #veľkost políčka
mriezka_x, mriezka_y = 10, 10 # x a y začiatku mriežky
vypln = 1
def kresli_mriezku(px, py, v, mx, my):
    for stlpec in range(px):
        for riadok in range(py):
            canvas.create_rectangle(stlpec*v + mx, riadok*v + my,(stlpec+1)*v + mx, (riadok+1)*v + my)
def kresli(stlpec, riadok, vypln):
    if vypln == 1:
        canvas.create_oval(stlpec*v + mriezka_x +1, riadok*v+mriezka_y+1,(stlpec+1)*v+mriezka_x -2, (riadok+1)*v+mriezka_y-2,fill = 'red')
    if vypln == 2:
        canvas.create_line(stlpec*v + mriezka_x +1, riadok*v+mriezka_y+1,(stlpec+1)*v+mriezka_x -1, (riadok+1)*v+mriezka_y+1,fill = 'blue', width = 2)
        canvas.create_line(stlpec*v + mriezka_x +1, (riadok+1)*v+mriezka_y+1,(stlpec+1)*v+mriezka_x -1, riadok*v + mriezka_y+1,fill = 'blue', width = 2)
def pozicia(x, y):
    stlpec = (x - mriezka_x) // v
    riadok = (y - mriezka_y) // v
    return stlpec, riadok
def oznac(sur):
    global vypln
    vypln = 3 - vypln
    stlpec, riadok = pozicia(sur.x, sur.y)
    kresli(stlpec, riadok, vypln)
kresli_mriezku(pocet_policok_x, pocet_policok_y, v, mriezka_x, mriezka_y)
canvas.bind('<Button-1>', oznac)


canvas.mainloop()
import tkinter

canvas = tkinter.Canvas(width=500, height=300)
canvas.pack()

pocet_zapaliek = 0
aktualny_hrac = 1
zoznam_tahov = []

def nakresli_zapalky():
    global pocet_zapaliek, aktualny_hrac, zoznam_tahov
    canvas.delete("zapal")
    canvas.delete("text")
    x = 0
    pocet_zapaliek = int(vstup.get())
    aktualny_hrac = 1
    zoznam_tahov = []
    canvas.create_text(250, 50, text="Hráč 1 je na ťahu", tags="text")
    for i in range(pocet_zapaliek):
        x += 40
        canvas.create_line(25 + x, 280, 25 + x, 100, fill="orange", width=8, tags="zapal")
        canvas.create_oval(10 + x, 100, 40 + x, 50, fill="red", outline="black", tags="zapal")

def odober1():
    odober(1)

def odober2():
    odober(2)

def odober3():
    odober(3)

def odober(mnozstvo):
    global pocet_zapaliek, aktualny_hrac
    if pocet_zapaliek == 0:
        return
    if mnozstvo > pocet_zapaliek:
        mnozstvo = pocet_zapaliek
    pocet_zapaliek -= mnozstvo
    zoznam_tahov.append((aktualny_hrac, mnozstvo))
    canvas.delete("zapal")
    canvas.delete("text")
    x = 0
    for i in range(pocet_zapaliek):
        x += 40
        canvas.create_line(25 + x, 280, 25 + x, 100, fill="orange", width=8, tags="zapal")
        canvas.create_oval(10 + x, 100, 40 + x, 50, fill="red", outline="black", tags="zapal")
    if pocet_zapaliek == 0:
        canvas.create_text(250, 50, text="Hráč " + str(aktualny_hrac) + " prehral! Vyhráva hráč " + str(3 - aktualny_hrac), tags="text")
    else:
        aktualny_hrac = 3 - aktualny_hrac
        canvas.create_text(250, 50, text="Hráč " + str(aktualny_hrac) + " je na ťahu", tags="text")

def reprisa():
    global pocet_zapaliek
    pocet_zapaliek = int(vstup.get())
    canvas.delete("zapal")
    canvas.delete("text")
    x = 0
    for i in range(pocet_zapaliek):
        x += 40
        canvas.create_line(25 + x, 280, 25 + x, 100, fill="gray", width=8, tags="zapal")
        canvas.create_oval(10 + x, 100, 40 + x, 50, fill="darkred", outline="black", tags="zapal")
    canvas.create_text(250, 50, text="Repríza začína...", tags="text")
    canvas.after(1000, lambda: animuj_reprisu(0))

def animuj_reprisu(krok):
    if krok < len(zoznam_tahov):
        hrac, mnozstvo = zoznam_tahov[krok]
        canvas.delete("text")
        canvas.create_text(250, 50, text=f"Hráč {hrac} zobral {mnozstvo} zápaliek", tags="text")
        canvas.after(1000, lambda: odstran_zapalky_anim(mnozstvo, krok + 1))
    else:
        canvas.delete("text")
        canvas.create_text(250, 50, text="Repríza skončená", tags="text")

def odstran_zapalky_anim(mnozstvo, krok):
    if mnozstvo > 0:
        zapalky = canvas.find_withtag("zapal")
        if len(zapalky) >= 2:
            canvas.delete(zapalky[-1], zapalky[-2])
            canvas.after(500, lambda: odstran_zapalky_anim(mnozstvo - 1, krok))
        else:
            animuj_reprisu(krok)
    else:
        animuj_reprisu(krok)

vstup = tkinter.Entry()
vstup.pack()

tlacidlo_start = tkinter.Button(text="Začni", command=nakresli_zapalky)
tlacidlo_start.pack()

canvas.create_text(250, 50, text="Zadaj počet zápaliek a klikni na 'Začni'", tags="text")

tlacidlo_o1 = tkinter.Button(text="Odober 1", command=odober1)
tlacidlo_o1.pack()

tlacidlo_o2 = tkinter.Button(text="Odober 2", command=odober2)
tlacidlo_o2.pack()

tlacidlo_o3 = tkinter.Button(text="Odober 3", command=odober3)
tlacidlo_o3.pack()

tlacidlo_reprisa = tkinter.Button(text="Repríza", command=reprisa)
tlacidlo_reprisa.pack()

canvas.mainloop()

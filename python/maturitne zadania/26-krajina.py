import tkinter
import random

canvas = tkinter.Canvas(width=800, height=400, bg='skyblue')
canvas.pack()

def kresli_krajinu(event=None):
    canvas.delete('all')
    # Opakovane vykreslíme niekoľko prvkov krajiny (napr. 6)
    for i in range(6):
        x_vrchol = random.randint(100, 700)
        y_aktualne = random.randint(250, 350)
        typ = random.randint(0, 1) # 0 pre kopec, 1 pre údolie
        
        body = [0, 400] # Začiatok v ľavom dolnom rohu
        
        # Generovanie bodov po 10 pixeloch na x-ovej osi
        for x in range(0, 810, 10):
            zmena = random.randint(0, 15)
            if typ == 0: # KOPEC
                if x < x_vrchol:
                    y_aktualne -= zmena # Stúpa (y sa zmenšuje)
                else:
                    y_aktualne += zmena # Klesá (y sa zväčšuje)
            else: # ÚDOLIE
                if x < x_vrchol:
                    y_aktualne += zmena # Klesá
                else:
                    y_aktualne -= zmena # Stúpa
            
            body.append(x)
            body.append(y_aktualne)
            
        body.append(800)
        body.append(400) # Koniec v pravom dolnom rohu
        
        # Náhodný odtieň zelenej
        zelena = random.randint(100, 255)
        farba = "#00" + hex(zelena)[2:].zfill(2) + "00"
        
        canvas.create_polygon(body, fill=farba, outline='black')

# Priradenie medzery
canvas.bind_all('<space>', kresli_krajinu)
kresli_krajinu() # Prvé vykreslenie
tkinter.mainloop()
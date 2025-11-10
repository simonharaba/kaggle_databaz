import tkinter
WIDTH, HEIGHT = 720, 480
canvas = tkinter.Canvas(width=WIDTH, height=HEIGHT, bg='white')
canvas.pack()
subor = 'sms.txt'
hlasy = [0] * 10
def citaj_subor(subor):
    f = open(subor, 'r')
    for cislo in f:
        cislo = int(cislo.strip())-6930
        hlasy[cislo] += 1
    f.close()
citaj_subor(subor)
pocet_hlasujucich = sum(hlasy)

hlasy2 = []
for i in range(len(hlasy)):
    hlasy2.append((hlasy[i], i+6930))
hlasy2.sort()

maxH = HEIGHT*2
def graf():
    x1 = WIDTH // (len(hlasy2)+1)
    y1 = HEIGHT-75
    canvas.create_text(WIDTH/2, 15, text='Hlasovalo: ' + str(pocet_hlasujucich) + ' ľudí.', font='Arial 12 bold', fill='#15791c')
    index = 10
    for info in hlasy2[::-1]:
        index -= 1
        sms = info[1]
        pocet = info[0]
        percento = (pocet/pocet_hlasujucich)*100
        percento = '{:.1f}%'.format(percento)
        y2 = int((pocet/pocet_hlasujucich)*maxH)
        canvas.create_rectangle(x1, y1, x1+28, y1-y2, fill='#4cb050')
        canvas.create_text(x1+14, y1+50, text=sms, font='Arial 12 bold', fill='#15791c')
        canvas.create_text(x1+14, y1-y2-8, text=pocet, font='Arial 8 bold', fill='#15791c')
        if index == 0:
            canvas.create_line(x1-5, y1-y2-72, x1+33, y1+5, width=5, fill='red')
            canvas.create_line(x1-5, y1+5, x1+33, y1-y2-72, width=5, fill='red')
            canvas.create_text(x1+15, y1+25, text=percento, font='Arial 12 bold', fill='red')
        else:
            canvas.create_text(x1+15, y1+25, text=percento, font='Arial 12 bold', fill='green')
        x1 += WIDTH // (len(hlasy2)+1)
graf()

canvas.mainloop()
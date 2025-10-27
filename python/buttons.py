import tkinter
def vypis():
    predmety = predmet1.get() + ' ' + predmet2.get() + ' ' + predmet3.get()
    predmety = predmety.strip()
    print('Práve máte vybraté predmety:', predmety)
label1 = tkinter.Label(text='Z ktorého predmetu idete maturovať?')
label1.pack()
predmet1 = tkinter.StringVar()
checkbutton1 = tkinter.Checkbutton(text='slovenský jazyk a literatúra',onvalue='SJL', offvalue='', variable=predmet1,command=vypis)
checkbutton1.pack(anchor='w')
predmet2 = tkinter.StringVar()
checkbutton2 = tkinter.Checkbutton(text='anglický jazyk', onvalue='AJ',offvalue='', variable=predmet2, command=vypis)
checkbutton2.pack(anchor='w')
predmet3 = tkinter.StringVar()
checkbutton3 = tkinter.Checkbutton(text='nemecký jazyk', onvalue='NJ',offvalue='', variable=predmet3, command=vypis)
checkbutton3.pack(anchor='w')

import tkinter
text1 = tkinter.Text(height=5, width=30)
text1.pack()
f = open('score.txt', 'r')
for riadok in f:
    text1.insert('end', riadok)
f.close()


v = tkinter.StringVar()
mesta = [('Banská Bystrica','BB'), ('Bratislava','BA'), ('Košice','KE'),('Nitra','NR'), ('Prešov','PO'), ('Trenčín','TN'), ('Trnava','TT'),('Žilina','ZA')]
label4 = tkinter.Label(text='Z kade si?')
label4.pack()
def vypis():
    print(v.get())
    
for mesto, skratka in mesta:
    rb = tkinter.Radiobutton(text=mesto, value=skratka,variable=v, command=vypis)
    
    rb.pack(anchor='w')



text1 = tkinter.Text(height=5, width=30)
text1.pack()
f = open('score.txt', 'r')
for riadok in f:
    text1.insert('end', riadok)
f.close()



canvas = tkinter.Canvas(width=440, height=200, bg='white')
canvas.pack()
rx, ry = 100, 50
x, y = 200, 100

def zmena1(event):
    global rx
    rx = scale1.get()
    canvas.delete('all')
    canvas.create_text(x, y,text='samo',tags='oval',font=('arial',rx))
    prekresli()
def zmena2(event):
    global ry
    ry = scale2.get()
    prekresli()
def prekresli():
    canvas.coords('oval',[rx+x  , ry+y/2])
scale1 = tkinter.Scale(from_=-200, to=200, orient='horizontal',length=400, command=zmena1)
scale1.pack()
scale1.set(rx)
scale2 = tkinter.Scale(from_=-100, to=100, orient='vertical',length=200, command=zmena2)
scale2.place(x=400, y=0)
scale2.set(ry)



def prefarbi(event):
    oznacene = listbox1.curselection()
    canvas['bg'] = listbox1.get(oznacene)
def pridaj():
    listbox1.insert('end', entry1.get())
def vymaz():
    oznacene = listbox1.curselection()
    if len(oznacene) == 1:
        listbox1.delete(oznacene)
listbox1 = tkinter.Listbox()
listbox1.pack()
farby = ['red', 'green', 'blue', 'orange', 'yellow', 'white']
for prvok in farby:
    listbox1.insert('end', prvok)
listbox1.bind('<Double-Button-1>', prefarbi)
label5 = tkinter.Label(text='Napíš názov farby:')
label5.pack()
entry1 = tkinter.Entry()
entry1.pack()
button_add = tkinter.Button(text='Pridaj farbu', command=pridaj)
button_add.pack()
button_delete = tkinter.Button(text='Vymaž označenú farbu', command=vymaz)

def otvor():
    pass
def uloz():
    pass
def oprograme():
    text_menu.place(x=100, y=100)
    button_menu.place(x=300, y=200)
def oprograme_zatvor():
    text_menu.place_forget()
    button_menu.place_forget()

menu1 = tkinter.Menu()
root = label1.winfo_toplevel()
root.config(menu=menu1)
menu2 = tkinter.Menu(menu1)
menu2.add_command(label='Otvoriť', command=otvor)
menu2.add_command(label='Uložiť', command=uloz)
menu2.add_separator()
menu2.add_command(label='Skončiť', command=root.destroy) # alebo quit
menu1.add_cascade(label='Súbor', menu=menu2)
menu3 = tkinter.Menu(menu1)
menu3.add_command(label='O programe', command=oprograme)
menu1.add_cascade(label='Pomocník', menu=menu3)
text_menu = tkinter.Text(height=5, width=42)
text_menu.insert('end', 'O programe\ntoto je program na ukážku používania menu\nverzia 1.0')
text_menu.config(state='disabled')
button_menu = tkinter.Button(text='Zatvor', command=oprograme_zatvor)

tkinter.mainloop()

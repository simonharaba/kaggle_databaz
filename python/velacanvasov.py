import tkinter as tk
from tkinter import messagebox




def otvor_canvas2():
    okno2=tk.Toplevel(root)
    okno2.title('Canvas 2')

    text1 = tk.Text(okno2, height=5, width=30)
    text1.pack()

    try:
        with open('x.txt', 'r') as f:
            for riadok in f:
                text1.insert('end', riadok)
    except FileNotFoundError:
        text1.insert('end', 'x.txt not found')




def otvor_canvas3():
    okno3=tk.Toplevel(root)
    okno3.title('Canvas 3')

    frame=tk.Frame(okno3)
    frame.pack(fill='both',expand=True)

    canvas3=tk.Canvas(okno3,width=400,height=300,bg='lightyellow')
    canvas3.pack(padx=10,pady=10)

    mesta = [('Banská Bystrica','BB'), ('Bratislava','BA'), ('Košice','KE'),('Nitra','NR'), ('Prešov','PO'), ('Trenčín','TN'), ('Trnava','TT'),('Žilina','ZA')]
    label = tk.Label(okno3, text='Z kade si?')
    canvas3.create_window(200, 20, window=label)
    v = tk.StringVar()
    def vypis():
        print(v.get())

    for i, (mesto, skratka) in enumerate(mesta):
        rb = tk.Radiobutton(okno3, text=mesto, value=skratka, variable=v, command=vypis)
        canvas3.create_window(200, 50 + i*30, window=rb)




def otvor_canvas4():
    okno4=tk.Toplevel(root)
    okno4.title('Canvas 4')

    canvas4=tk.Canvas(okno4,width=400,height=300,bg='white')
    canvas4.pack(padx=10,pady=10)

    def prefarbi(event):
        oznacene = listbox1.curselection()
        canvas4['bg'] = listbox1.get(oznacene)

    def pridaj():
        listbox1.insert('end', entry1.get())

    def vymaz():
        oznacene = listbox1.curselection()
        if len(oznacene) == 1:
            listbox1.delete(oznacene)

    listbox1 = tk.Listbox(okno4)
    canvas4.create_window(200, 100, window=listbox1)
    farby = ['red', 'green', 'blue', 'orange', 'yellow', 'white']

    for prvok in farby:
        listbox1.insert('end', prvok)
    listbox1.bind('<Double-Button-1>', prefarbi)

    label1 = tk.Label(okno4, text='Napíš názov farby:')
    canvas4.create_window(200, 200, window=label1)

    entry1 = tk.Entry(okno4)
    canvas4.create_window(200, 220, window=entry1)

    button1 = tk.Button(okno4, text='Pridaj farbu', command=pridaj)
    canvas4.create_window(200, 240, window=button1)

    button2 = tk.Button(okno4, text='Vymaž označenú farbu', command=vymaz)
    canvas4.create_window(200, 260, window=button2)


def otvor_canvas5():
    okno5=tk.Toplevel(root)
    okno5.title('Canvas 5')

    frame=tk.Frame(okno5)
    frame.pack(fill='both',expand=True)

    canvas5=tk.Canvas(okno5,width=400,height=300,bg='lightyellow',scrollregion=(0,0,800,1200))
    canvas5.pack(padx=10,pady=10)

    v_scroll=tk.Scrollbar(frame,orient='vertical',command=canvas5.yview)
    v_scroll.pack(side='left',fill='both',expand=True)

    h_scroll=tk.Scrollbar(okno5,orient='horizontal',command=canvas5.xview)
    h_scroll.pack(side='bottom',fill='x')

    canvas5.configure(yscrollcommand=v_scroll.set,xscrollcommand=h_scroll.set)

    for i in range(30):
        canvas5.create_text(100,40*i+20,text=f'polozka cislo {i+1}',font=('Arial',14))
        canvas5.create_rectangle(200,40*i,380,40*i+30,fill='orange',outline='red')


def otvor_canvas6():
    okno6=tk.Toplevel(root)
    okno6.title('Canvas 6')

    def vypis():
        predmety = predmet1.get() + ' ' + predmet2.get() + ' ' + predmet3.get()
        predmety = predmety.strip()
        print('Práve máte vybraté predmety:', predmety)

    label1 = tk.Label(okno6, text='Z ktorého predmetu idete maturovať?')
    label1.pack()

    predmet1 = tk.StringVar()
    checkbutton1 = tk.Checkbutton(okno6, text='slovenský jazyk a literatúra',
                  onvalue='SJL', offvalue='', variable=predmet1,
                  command=vypis)
    checkbutton1.pack(anchor='w')

    predmet2 = tk.StringVar()
    checkbutton2 = tk.Checkbutton(okno6, text='anglický jazyk', onvalue='AJ', offvalue='', variable=predmet2, command=vypis)
    checkbutton2.pack(anchor='w')

    predmet3 = tk.StringVar()
    checkbutton3 = tk.Checkbutton(okno6, text='nemecký jazyk', onvalue='NJ',
                  offvalue='', variable=predmet3, command=vypis)
    checkbutton3.pack(anchor='w')


root=tk.Tk()
root.title('Hlavne okno')




menu_bar=tk.Menu(root)
root.config(menu=menu_bar)

zobrazit_menu = tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='zobrazit',menu=zobrazit_menu)



zobrazit_menu.add_command(label='Canvas 2',command=otvor_canvas2)
zobrazit_menu.add_command(label='Canvas 3',command=otvor_canvas3)
zobrazit_menu.add_command(label='Canvas 4',command=otvor_canvas4)
zobrazit_menu.add_command(label='Canvas 5',command=otvor_canvas5)
zobrazit_menu.add_command(label='Canvas 6',command=otvor_canvas6)











canvas1 = tk.Canvas(root, width=400, height=100, bg='white')
canvas1.pack()

def oznam():
    vysledok = messagebox.showinfo('oznam', 'stlačili ste tlačidlo')
    print(vysledok)

def otazka1():
    vysledok = messagebox.askyesno('Pokračovanie', 'Chcete pokračovať?')
    print(vysledok)

def otazka2():
    vysledok = messagebox.askyesnocancel('Pokračovanie', 'Chcete pokračovať?')
    print(vysledok)

button1 = tk.Button(root, text='zobraz oznam', command=oznam)
button1.pack()

button2 = tk.Button(root, text='otazka 1', command=otazka1)
button2.pack()

button3 = tk.Button(root, text='otazka 2', command=otazka2)
button3.pack()



root.mainloop()



import tkinter as tk
def otvor_canvas2():
    okno2=tk.Toplevel(root)
    okno2.title('Canvas 2')

    canvas2=tk.Canvas(okno2,width=400,height=300,bg='lightyellow')
    canvas2.pack(padx=10,pady=10)

    canvas2.create_oval(50,50,200,200,fill='orange',outline='red')
    canvas2.create_text(200.,250,text='Toto je Canvas 2',font=('Arial',14,'bold'))

def otvor_canvas3():
    okno3=tk.Toplevel(root)
    okno3.title('Canvas 3')

    canvas3=tk.Canvas(okno3,width=400,height=300,bg='lightyellow')
    canvas3.pack(padx=10,pady=10)
    
    mesta = [('Banská Bystrica','BB'), ('Bratislava','BA'), ('Košice','KE'),('Nitra','NR'), ('Prešov','PO'), ('Trenčín','TN'), ('Trnava','TT'),('Žilina','ZA')]
    label = tk.Label(text='Z kade si?')
    label.pack()
    def vypis():
        print(v.get())
    
    for mesto, skratka in mesta:
        rb = tk.Radiobutton(text=mesto, value=skratka,variable=v, command=vypis)
    
        rb.pack(anchor='w')


def otvor_canvas4():
    okno4=tk.Toplevel(root)
    okno4.title('Canvas 4')

    canvas4=tk.Canvas(okno4,width=400,height=300,bg='lightyellow')
    canvas4.pack(padx=10,pady=10)

    canvas4.create_oval(50,50,200,200,fill='orange',outline='red')
    canvas4.create_text(200.,250,text='Toto je Canvas 4',font=('Arial',14,'bold'))




root=tk.Tk()
root.title('Hlavne okno')

menu_bar=tk.Menu(root)
root.config(menu=menu_bar)

zobrazit_menu = tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='zobrazit',menu=zobrazit_menu)

zobrazit_menu.add_command(label='Canvas 2',command=otvor_canvas2)
zobrazit_menu.add_command(label='Canvas 3',command=otvor_canvas3)
zobrazit_menu.add_command(label='Canvas 4',command=otvor_canvas4)


canvas1=tk.Canvas(root,width=400,height=300,bg='white')
canvas1.pack()
canvas1.create_rectangle(50,50,200,200,fill='lightblue',outline='blue')
canvas1.create_text(200,250,text='Toto je Canvas 1', font=('Arial',14,'bold'))






canvas1.mainloop()

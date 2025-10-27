import tkinter
canvas=tkinter.Canvas(height='200',width='400')
canvas.pack()
cislo=()
od=0
do=0
pokusy=0
x=300
y=100


def ratanie():
    global cislo,od,do,pokusy,pokusy,x,y
    od = int(entry1.get())
    do = int(entry2.get())
    cislo=(do-od)//2+od
    pokusy+=1
    canvas.delete('all')
    canvas.create_text(x-170,y,text='Je toto tvoje cislo?',font='Arial 20')
    canvas.create_text(x,y,text=cislo,font='Arial 20')
    canvas.create_text(x,y+50,text=str(pokusy))
    canvas.create_text(x-50,y+50,text='Pocet pokusov:')

def vacsie():    
    global cislo,od,do,pokusy,x,y
    od = cislo+1
    canvas.delete('all')
    pokusy+=1
    cislo = (do-od)//2+od
    canvas.create_text(x-170,y,text='Je toto tvoje cislo?',font='Arial 20')
    canvas.create_text(x,y,text=cislo,font='Arial 20') 
    canvas.create_text(x,y+50,text=str(pokusy))
    canvas.create_text(x-50,y+50,text='Pocet pokusov:')

def mensie():    
    global cislo,do,od,pokusy,x,y
    do = cislo
    canvas.delete('all')
    pokusy+=1
    cislo=(do-od)//2+od
    canvas.create_text(x-170,y,text='Je toto tvoje cislo?',font='Arial 20')
    canvas.create_text(x,y,text=cislo,font='Arial 20')
    canvas.create_text(x,y+50,text=str(pokusy))
    canvas.create_text(x-50,y+50,text='Pocet pokusov:')


entry1=tkinter.Entry()
entry1.pack()
entry1.insert(0,'mensie')
entry2=tkinter.Entry()
entry2.pack()
entry2.insert(0,'vacsie')

button1 = tkinter.Button(text='Potvrd',command=ratanie)
button1.pack()

button2 = tkinter.Button(text='vacsie',command=vacsie)
button2.pack()
button3 = tkinter.Button(text='mensie',command=mensie)
button3.pack()


canvas.mainloop()
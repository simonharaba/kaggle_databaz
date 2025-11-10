import tkinter
canvas=tkinter.Canvas()

text1 = tkinter.Text(height=5, width=30)
text1.pack()
text1.pack(side='left')
with open('prihlaseni.txt','r') as subor:
    with open('mena.txt','w') as subor2:
        riadky=subor.readlines()
        for riadok in range(0,len(riadky),2):
            subor2.write(riadky[riadok])
            text1.insert('end',riadky[riadok])
canvas.pack()
canvas.mainloop()


    


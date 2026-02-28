import tkinter
canvas=tkinter.Canvas(width=500,height=500,bg='white')
canvas.pack()


def histogram(hodnoty,miera):
    for i in range(256):
        canvas.create_rectangle(i*2,500,i*2+2,500-hodnoty[i]/miera,width=0,fill='grey')
subor=open('31-ciernobielyobrazok.txt','r')
riadok=subor.readline()
velkost=riadok.split()
sirka=int(velkost[0])
vyska=int(velkost[1])

odtiene=[0]*256
for i in range(vyska):
    riadok=subor.readline()
    for j in range(sirka):
        farba=riadok[j*2:j*2+2]
        dec_farba=int(farba,16)
        odtiene[dec_farba]+=1
subor.close()
max_vyskyt=max(odtiene)
mierka=(max_vyskyt/500)+1
histogram(odtiene,mierka)
canvas.mainloop()
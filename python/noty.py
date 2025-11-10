#noty
import tkinter
canvas=tkinter.Canvas(width=400,height=400)
canvas.pack()



subor=open('noty.txt','r')
riadok=subor.read().strip()


pocet=0
y=50
for i in range(4):
    canvas.create_line(0,50+i*20,500,50+i*20)

def noty():
    global x,y
    y=30
    x=0
    
    pocet=0
    
    for znak in riadok:
    
            
        
        if pocet<20:
            if znak=='c':
                pocet+=1
                canvas.create_oval(x,y+70,x+10,y+80)
            elif znak=='d':
                pocet+=1
                canvas.create_oval(x,y+60,x+10,y+70)
            elif znak=='e':
                pocet+=1
                canvas.create_oval(x,y+50,x+10,y+60)
            elif znak=='f':
                pocet+=1
                canvas.create_oval(x,y+40,x+10,y+50)
            elif znak=='g':
                pocet+=1
                canvas.create_oval(x,y+30,x+10,y+40)
            elif znak=='h':
                pocet+=1
                canvas.create_oval(x,y+20,x+10,y+30)
        
            x+=20
        else:
            
            pocet=pocet-20
            y+=100
            x=x-400
            for i in range(4):
                canvas.create_line(0,y+10+i*20,500,y+10+i*20)

noty()
canvas.mainloop()
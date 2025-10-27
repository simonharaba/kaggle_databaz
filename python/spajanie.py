subor=open('kreslenie.txt','r')
subor2=open('suradnice.txt','w')

riadky=subor.readlines()

for riadok in range(0,len(riadky),2):
    x=riadky[riadok].strip()
    y=riadky[riadok+1].strip()
    subor2.write(x+','+y+'\n')
    
    

#12 autobus

subor=open('bus_vytazenost.txt','r')
zastavka=0
mena=[]
najviac=0
for riadok in subor:
    zastavka+=1
    pocet=riadok.split()
    if pocet[0]=='50':
        kapacita=int(pocet[0])
        print("Kapacita autobusu je",kapacita,"miest.")
    else:
        nastupilo=int(pocet[0])
        vystupilo=int(pocet[1])
        nazov=pocet[2]
        mena.append(nazov)
        nastupilo-=vystupilo
        najviac+=nastupilo
        
        if najviac>kapacita:
            print('Na zastavke',nazov,'nastupilo',nastupilo,'takze prekrocili kapacitu o',najviac-kapacita,'miest.')
        

            

print('Pocet zastavok:',zastavka-1)
print('Nazov zastavky',mena)
print('Maximalne vytazenost autobusu bola',najviac,'miest.')

def spracuj_riadok(vstup):
    pocet=len(vstup)//2
    vystup=''
    for i in range(pocet):
        odtien=vstup[i*2:i*2+2]
        farba='0'
        if odtien>'7f':
            farba='1'
        vystup+=farba+' '
    vystup=vystup[:-1]+'\n'
    return vystup
subor=open('31-ciernobielyobrazok.txt','r')
subor_vystup=open('32-vystup.txt','w')
riadok=subor.readline()
velkost=riadok.split()
subor_vystup.write(riadok)
sirka=int(velkost[0])
vyska=int(velkost[1])
print('obrazok ma sirku',sirka,'a vysku',vyska)
print('obrazok ma',sirka*vyska,'bodov')
riadok=subor.readline()
print(repr(riadok))
spracovanie=spracuj_riadok(riadok)
print(repr(spracovanie))
subor_vystup.write(spracovanie)
for riadok in subor:
    subor_vystup.write(spracuj_riadok(riadok))
subor.close()
subor_vystup.close()
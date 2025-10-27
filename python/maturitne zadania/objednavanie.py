vstup=open('objednavanie_jedla.txt','r')
pocet=0
z,c,m,o=0,0,0,0
for riadok in vstup:
    pocet+=1
    riadok=riadok.strip()
    if riadok[-1]=='z':
        z+=1
    elif riadok[-1]=='c':
        c+=1
    elif riadok[-1]=='m':
        m+=1
    else:
        o+=1


print('pocet objednanych jedal:',pocet)
print('zelene jedlo bolo objednane:',z,'krat')
print('cervene jedlo bolo objednane:',c,'krat')
print('modre jedlo bolo objednane:',m,'krat')
print('oranzove jedlo bolo objednane:',o,'krat')


if z<20:
    print('Zelenych jedal bolo objednanych menej ako 20')
if c<20:
    print('Cervenych jedal bolo objednanych menej ako 20')
if m<20:
    print('Modrych jedal bolo objednanych menej ako 20')
if o<20:
    print('Oranzovych jedal bolo objednanych menej ako 20')

if z>=20 and c>=20 and m>=20 and o>=20:
    print('bol objednany spravny pocet jedal kazdeho druhu')
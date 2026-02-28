subor=open('34-vstup.txt','r')
subor_vystup=open('34-vystup.txt','w')
riadok1=subor.readline()
velkost=riadok1.split()
sirka=int(velkost[0])
vyska=int(velkost[1])
subor_vystup.write(str(sirka) + ' ' + str(vyska) + '\n')

def dekompresia():
    for riadok in subor:
        tokens = riadok.split()
        aktualny = 1
        for znak in tokens:
            if znak == '':
                continue
            cnt = int(znak)
            subor_vystup.write(str(aktualny) * cnt)
            aktualny = 1 - aktualny
        subor_vystup.write('\n')

dekompresia()
subor.close()
subor_vystup.close()
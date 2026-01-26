import random
def pomiesaj(retazec):
    pismenka=list(retazec)
    random.shuffle(pismenka)
    return ''.join(pismenka)
def ocisti_slovo(slovo):
    ciste_slovo=''
    zly_zaciatok=''
    zly_koniec=''
    i=0
    while slovo[i] in vynechat:
        zly_zaciatok+=slovo[i]
        i+=1
    while i<len(slovo) and not (slovo[i] in vynechat):
        ciste_slovo+=slovo[i]
        i+=1
    zly_koniec=slovo[i:]
    return zly_zaciatok,ciste_slovo,zly_koniec
vynechat=' ,.!?;:-_\'"()[]{}<>«»„“”‘’´`´\n\t'
subor1=open('22-prehoditdiakritika-vstup.txt','r',encoding='utf-8')
subor2=open('22-prehoditdiakritika-vystup.txt','w',encoding='utf-8')
for riadok in subor1:
    print(riadok,end='')
    slova=riadok.strip().split()
    for i in range(len(slova)):
        pred,stred,koniec=ocisti_slovo(slova[i])
        if len(stred)>2:
            stred=stred[0]+pomiesaj(stred[1:-1])+stred[-1]
        slova[i]=pred+stred+koniec
    riadok=' '.join(slova)+'\n'
    print(riadok,end='')
    subor2.write(riadok)
subor1.close()
subor2.close()

#priebeh_hadik
subor=open('hada.txt','r',encoding='utf-8')
subor2=open('hadkompres.txt','w')
pocet=0
max=0
def kompresia(s):
    if s=='':
        return ''
    s=s+'.'
    pismeno=s[0]
    pocet=0
    vystup=''
    for znak in s:
        if znak==pismeno:
            pocet+=1
        else:
            vystup=vystup+'{} {}'.format(pismeno,pocet)
            pismeno=znak
            pocet=1
    return vystup
for riadok in subor:
    riadok=riadok.strip()
    print(riadok)
    riadok2=kompresia(riadok)
    subor2.write(riadok2+'\n')
    print(riadok2)
    if len(riadok)>max:
        max=len(riadok)
    pocet+=1
print('pocet riadkov v subore:',pocet)
print('pocet prvkov v najdlhsej hre:',max)
subor.close()
subor2.close()

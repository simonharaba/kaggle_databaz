import random
vstup=open('24-vstupnytext.txt','r',encoding='utf-8')
kluc=open('24-zasifrovanytext.txt','w',encoding='utf-8')
abeceda='abcdefghijklmnopqrstuvwxyz'

for riadok in vstup:
    cislo=random.randrange(1,26)
    vystup=''
    
    for znak in riadok:
        if znak==' ':
            vystup+=' '
        elif znak.lower() in abeceda:
            index=(ord(znak.lower())-ord('a')+cislo)%26
            novy_znak=abeceda[index]
            if znak.isupper():
                novy_znak=novy_znak.upper()
            vystup+=novy_znak
        else:
            vystup+=znak
    
    kluc.write(vystup)    
    print(vystup, end='')

kluc.close()
vstup.close()

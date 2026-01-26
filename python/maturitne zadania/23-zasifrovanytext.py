vstup=open('23-vstupnytext.txt','r',encoding='utf-8').read()
kluc=open('23-zasifrovanytext.txt','r',encoding='utf-8').read().strip()
abeceda='abcdefghijklmnopqrstuvwxyz'
vystup=''
pozicia_kluca=0

for znak in vstup:
    if znak==' ':
        vystup+='-'
    elif znak.lower() in abeceda:
        shift=ord(kluc[pozicia_kluca%len(kluc)])-ord('a')
        index=(ord(znak.lower())-ord('a')+shift+1)%26
        novy_znak=abeceda[index]
        if znak.isupper():
            novy_znak=novy_znak.upper()
        vystup+=novy_znak
        pozicia_kluca+=1
    else:
        vystup+=znak

print(vystup)
    

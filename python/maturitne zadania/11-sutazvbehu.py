#11 sutaz v behu
subor=open("sutaz_vbehu.txt","r")
najrychlejsi=9999999
pocet=0
for riadok in subor:
    pocet+=1
    bezec=riadok.split()
    meno=bezec[0]
    cas=int(bezec[1])
    print('Sutaziaci',meno,'behol cas',cas,'sekund.')
    if cas<najrychlejsi:
        najrychlejsi=cas
        najlepsie_meno=meno
    
minuty=najrychlejsi//60
sekundy=najrychlejsi%60
print("Počet bežcov v súťaži:",pocet)

print("Najrychlejší bežec je",najlepsie_meno,"s časom",minuty,':',sekundy,'.')
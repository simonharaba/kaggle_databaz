import random
spravne_cisla=''
pocet=0
for i in range(6):
    cislo=random.randrange(1,50)
    while str(cislo) in spravne_cisla.split():
        cislo=random.randrange(1,50)
    spravne_cisla+=str(cislo)+' '
print('Správne čísla sú:',spravne_cisla.strip())

uzivatel=input('Zadajte 6 tipov (oddelené medzerami): ').split()
uhadvane=0
for tip in uzivatel:
    if tip in spravne_cisla.split():
        uhadvane+=1
print('Uhádnuté čísla:',uhadvane)

pocty_zhod={1:0, 2:0, 3:0, 5:0, 6:0}
subor=open('25-loteria.txt','r',encoding='utf-8')
for riadok in subor:
    udaje=riadok.strip().split()
    pocet_zhod=0
    for tip in udaje:
        if tip in spravne_cisla.split():
            pocet_zhod+=1
    if pocet_zhod in pocty_zhod:
        pocty_zhod[pocet_zhod]+=1

subor.close()

print('\nŠtatistika:')
if pocty_zhod[1]>0:
    print('Práve 1 číslo:',pocty_zhod[1])
if pocty_zhod[2]>0:
    print('Práve 2 čísla:',pocty_zhod[2])
if pocty_zhod[3]>0:
    print('Práve 3 čísla:',pocty_zhod[3])
if pocty_zhod[5]>0:
    print('Práve 5 čísel:',pocty_zhod[5])
if pocty_zhod[6]>0:
    print('Práve 6 čísel:',pocty_zhod[6])
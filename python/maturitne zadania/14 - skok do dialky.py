#14 skok do dialky

subor=open('skok_do_dialky.txt','r')
mena=[]
najvacsie=0
najlepsi=[]
krajiny=[]
for riadok in subor:
    rozdel=riadok.split()
    mena.append(rozdel[0])
    meno=rozdel[0]
    krajina=rozdel[1]
    krajiny.append(krajina)
    pocty=rozdel[2:7]
    
    
    print(meno,pocty)
    for i in range(5):
        if int(pocty[i])>najvacsie:
            najvacsie=int(pocty[i])
            najlepsi=[meno]
        elif int(pocty[i])==najvacsie:
            if meno not in najlepsi:
                najlepsi.append(meno)
print(krajiny)
print("Najvacsie skoky do dialky su:", najvacsie, "dosiahli skokani:", ", ",najlepsi)

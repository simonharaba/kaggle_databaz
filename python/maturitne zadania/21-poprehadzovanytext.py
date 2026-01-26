#21. Poprehadzovaný text
from random import*
vstup=open('21-poprehadzovany_text1.txt','r',encoding='utf-8')
text=[]
for line in vstup:
    text.append(line.strip().split())
vstup.close()

vystup=''
for line in text:
    for word in line:
        newword=list(word[1:-1])
        shuffle(newword)
        newword=word[0]+''.join(newword)+word[-1]
        vystup=vystup+newword+' '
    vystup=vystup+'\n'
print(vystup)
vystupT=open('21-poprehadzovanytext_vystup1.txt','w',encoding='utf-8')
vystupT.write(vystup)
vystupT.close()
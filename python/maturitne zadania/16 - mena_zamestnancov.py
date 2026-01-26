#16 mena zamestnancov

subor=open('16-mena_zamestnancov.txt','r',encoding='utf-8')
mena=subor.readlines()
subor.close()
for i in range(len(mena)):
    mena[i]=mena[i].strip()
pocet=len(mena)//2
print(pocet)
krstne=mena[:pocet]
priezviska=mena[pocet:]
dlzka=0
for s in priezviska:
    dlzka=max(dlzka,len(s))
print('Najdlhsie priezvisko ma',dlzka,'znakov.')
for s in krstne:
    dlzka=max(dlzka,len(s))
print('Najdlhsie krstne ma',dlzka,'znakov.')
vystup=open('16-vystup.txt','w',encoding='utf-8')
for i in range(pocet):
    vystup.write(krstne[i] + ' ' * (dlzka - len(krstne[i]) + 1) + priezviska[i] + '\n')
vystup.close()
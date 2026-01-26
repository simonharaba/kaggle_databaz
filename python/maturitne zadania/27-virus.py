import random

# 1. Prečítanie súboru do zoznamu riadkov
f_in = open('27-virus.txt', 'r', encoding='utf-8')
riadky = f_in.readlines()
f_in.close()

# 2. Náhodné rozhodnutie o zmene poradia riadkov
if random.randint(0, 1) == 1:
    random.shuffle(riadky)

vysledok = []

for riadok in riadky:
    slova = riadok.split()
    
    # 3. Náhodné rozhodnutie o zmene poradia slov v riadku
    if random.randint(0, 1) == 1:
        random.shuffle(slova)
        
    # 4. Náhodné rozhodnutie o otočení každého slova
    novy_riadok_slova = []
    for slovo in slova:
        if random.randint(0, 1) == 1:
            novy_riadok_slova.append(slovo[::-1]) # Otočenie slova
        else:
            novy_riadok_slova.append(slovo)
            
    vysledok.append(' '.join(novy_riadok_slova))

# 5. Uloženie do súboru
f_out = open('27-virus_vystup.txt', 'w', encoding='utf-8')
for r in vysledok:
    f_out.write(r + '\n')
f_out.close()

print("Transformácia dokončená.")
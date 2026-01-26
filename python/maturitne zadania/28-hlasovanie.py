# 1. Načítanie hlasov zo súboru
f = open('28-hlasovanie_1.txt', 'r')
vsetky_hlasy = []
for riadok in f:
    hlas = int(riadok.strip())
    vsetky_hlasy.append(hlas)
f.close()

# Celkový počet zaslaných SMS
print("Celkový počet zaslaných SMS:", len(vsetky_hlasy))

# 2. Koľko hlasov dostal každý (indexy 0-9 zodpovedajú číslam 5220-5229)
pocty = [0] * 10
for h in vsetky_hlasy:
    index = h - 5220
    if 0 <= index <= 9:
        pocty[index] = pocty[index] + 1

for i in range(10):
    print("Súťažiaci", 5220 + i, "dostal", pocty[i], "hlasov")

# 3. Najmenej hlasov celkovo (kto nepostupuje)
min_hlasov = pocty[0]
kto_vypadava = 5220
for i in range(1, 10):
    if pocty[i] < min_hlasov:
        min_hlasov = pocty[i]
        kto_vypadava = 5220 + i
print("Najmenej hlasov celkovo dostal:", kto_vypadava)

# 4. Najmenej hlasov bez započítania už vypadnutých
f_vyp = open('28-hlasovanie_vypadnuti.txt', 'r')
vypadnuti = []
for riadok in f_vyp:
    vypadnuti.append(int(riadok.strip()))
f_vyp.close()

min_aktivni = 99999999 # Veľké číslo na začiatok
kto_vypadava_teraz = -1

for i in range(10):
    cislo = 5220 + i
    # Skontrolujeme, či súťažiaci už nie je v zozname vypadnutých
    je_vypadnuty = False
    for v in vypadnuti:
        if cislo == v:
            je_vypadnuty = True
    
    # Ak nie je vypadnutý, porovnáme jeho počet hlasov
    if je_vypadnuty == False:
        if pocty[i] < min_aktivni:
            min_aktivni = pocty[i]
            kto_vypadava_teraz = cislo

print("Súťažiaci, ktorý nepostupuje (bez už vypadnutých):", kto_vypadava_teraz)
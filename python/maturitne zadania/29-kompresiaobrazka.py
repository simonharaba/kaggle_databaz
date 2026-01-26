def spracuj_riadok(riadok):
    vystup = ""
    aktualny = '0' # Podľa zadania začíname vždy sledovaním núl
    pocet = 0
    
    for znak in riadok:
        if znak == aktualny:
            pocet = pocet + 1
        else:
            # Ak sa znak zmení, zapíšeme doterajší počet
            vystup = vystup + str(pocet) + " "
            pocet = 1
            # Prepnutie medzi '0' a '1'
            if aktualny == '0':
                aktualny = '1'
            else:
                aktualny = '0'
    
    # Zápis poslednej série
    vystup = vystup + str(pocet)
    return vystup

# Otvorenie súborov
f_in = open('29-kompresia_obrazka_1.txt', 'r')
f_out = open('29-kompresia_obrazka_vystup.txt', 'w')

# 1. Prečítanie rozmerov
prvy_riadok = f_in.readline().split()
sirka = int(prvy_riadok[0])
vyska = int(prvy_riadok[1])

print("Šírka:", sirka)
print("Výška:", vyska)
print("Počet všetkých bodov:", sirka * vyska)

# Zápis rozmerov do výstupného súboru
f_out.write(str(sirka) + " " + str(vyska) + "\n")

# 2. + 3. Spracovanie všetkých riadkov obrázka
for riadok in f_in:
    cisty_riadok = riadok.strip()
    if cisty_riadok != "":
        komprimovany = spracuj_riadok(cisty_riadok)
        f_out.write(komprimovany + "\n")

f_in.close()
f_out.close()
print("Súbor kompresia_obrazka_vystup.txt bol vytvorený.")
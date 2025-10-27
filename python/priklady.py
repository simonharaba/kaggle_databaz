from random import*
max_prikladov = 5
priklady = []
vysledky = []
pouzite = []

# generovanie unikátnych príkladov
while len(priklady) < max_prikladov:
    a = randint(1, 20)
    b = randint(1, 20)
    op = choice(["+", "*"])

    priklad = str(a) + " " + op + " " + str(b)
    
    if op == "+":
        vysledok = a + b
    else:
        vysledok = a * b

    if priklad not in pouzite:
        pouzite.append(priklad)
        priklady.append(priklad)
        vysledky.append(vysledok)

        # riešenie príkladov
body = 0
ulozene = []

print("Vypočítaj nasledujúce príklady:\n")

for i in range(len(priklady)):
    odpoved = int(input(str(i+1) + ") " + priklady[i] + " = "))
    
    if odpoved == vysledky[i]:
        print("Správne!\n")
        body += 1
    else:
        print("Nesprávne! Správna odpoveď je", vysledky[i], "\n")
ulozene.append(str(i+1) + ") " + priklady[i] + " = " + str(odpoved) + " (správne: " + str(vysledky[i]) + ")")

# výsledky
print("Tvoje skóre:", body, "/", len(priklady))
uspech = body * 100 // len(priklady) # celé percentá
print("Úspešnosť:", uspech, "%")

subor=open('priklady.txt','w')
subor.write(str(priklady+vysledky))
subor.close()
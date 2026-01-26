#17 sifra

vstup = input().rstrip('\n')
vstup = vstup.upper()
policka = [" ", "ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "YZ"]

zakodovane = []
counts = {}
for d in range(10):
    counts[str(d)] = 0

for ch in vstup:
    if ch == ' ':
        kod = '0'
        zakodovane.append(kod)
        counts['0'] += 1
        continue

    
    found = False
    for i in range(1, 10):
        pole = policka[i]
        if ch in pole:
            pos = pole.index(ch)  
            kod = str(i) * (pos + 1)
            zakodovane.append(kod)
            counts[str(i)] += len(kod)
            found = True
            break
    if not found:
        pass


vystup = ' '.join(zakodovane)
print(vystup)


if len(vystup) == 0:
    print('Najčastejšie zvolené políčka:')
else:
    maxpocet = max(counts.values())

    naj = []
    for d, c in counts.items():
        if c == maxpocet and c > 0:
            naj.append(d)
    naj.sort()
    print('Najčastejšie zvolené políčka:', ' '.join(naj))

    
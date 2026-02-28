def uloha_38():
    spokojni = [0] * 24
    nespokojni = [0] * 24
    celkovo = 0

    # Otvorenie a načítanie súboru
    try:
        subor = open('38-spokojnost.txt', 'r', encoding='utf-8')
        for riadok in subor:
            if riadok.strip():
                cas, vyjadrenie = riadok.split()
                hodina = int(cas.split(':')[0])
                
                celkovo += 1
                if vyjadrenie == 'áno':
                    spokojni[hodina] += 1
                else:
                    nespokojni[hodina] += 1
        subor.close()

        # 1. Celkový počet vyjadrení
        print(f"Celkový počet vyjadrení: {celkovo}")

        # 2. Najviac spokojných
        max_ano = max(spokojni)
        h_max_ano = spokojni.index(max_ano)
        print(f"Najviac spokojných zákazníkov: {max_ano} (v hodine {h_max_ano:02d})")

        # 3. Najviac nespokojných
        max_nie = max(nespokojni)
        h_max_nie = nespokojni.index(max_nie)
        print(f"Najviac nespokojných zákazníkov: {max_nie} (v hodine {h_max_nie:02d})")

        # 4. Percentá spokojnosti pre hodiny s vyjadreniami
        print("\nPercentuálna spokojnosť podľa hodín:")
        for h in range(24):
            spolu_h = spokojni[h] + nespokojni[h]
            if spolu_h > 0:
                percento = (spokojni[h] / spolu_h) * 100
                print(f"Hodina {h:02d}: {percento:.1f}% spokojných")
    
    except FileNotFoundError:
        print("Súbor spokojnost_1.txt sa nenašiel.")

uloha_38()
#40 analyza udajov
def hlbkova_analyza():
    f = open('40-spokojnost_1.txt', 'r')
    
    pocet_dni = 0
    reakcie_v_dni = 0
    celkovo = 0
    hodiny_sumar = [0] * 24
    predchadzajuci_cas_minuty = 9999 # Inicializácia pre prvý riadok

    vystup_dni = []

    for riadok in f:
        cas_str, _ = riadok.split()
        h, m = map(int, cas_str.split(':'))
        aktualny_cas_minuty = h * 60 + m
        
        # Ak je čas menší ako predchádzajúci, začal nový deň
        if aktualny_cas_minuty < predchadzajuci_cas_minuty:
            if pocet_dni > 0:
                vystup_dni.append(reakcie_v_dni)
            pocet_dni += 1
            reakcie_v_dni = 0
            
        reakcie_v_dni += 1
        celkovo += 1
        hodiny_sumar[h] += 1
        predchadzajuci_cas_minuty = aktualny_cas_minuty

    f.close()
    vystup_dni.append(reakcie_v_dni) # Pridanie posledného dňa

    # Výpis výsledkov
    for i, r in enumerate(vystup_dni):
        print(f"{i+1}. deň - počet reakcií: {r}")
    
    print(f"Počet všetkých vyjadrení: {celkovo}")
    
    for h in range(24):
        if hodiny_sumar[h] > 0:
            print(f"Hodina:{h} Reakcií zákazníkov:{hodiny_sumar[h]}")
            
    print(f"Počet dní: {pocet_dni}")

hlbkova_analyza()
def spracuj_hlasovanie():
    f = open('37-hlasovanie.txt', 'r')
    hlasy = f.readlines()
    f.close()

    print(f"Celkový počet zaslaných SMS: {len(hlasy)}")

    # Otvoríme súbory pre všetkých možných súťažiacich (5220-5229)
    subory = {}
    for i in range(5220, 5230):
        subory[str(i)] = open(f'{i}.txt', 'w')

    for index, cislo in enumerate(hlasy):
        cislo = cislo.strip()
        if cislo in subory:
            # index + 1, pretože poradové čísla rátame od 1
            subory[cislo].write(f"{index + 1}\n")

    # Zatvoríme všetky otvorené súbory
    for s in subory.values():
        s.close()

spracuj_hlasovanie()
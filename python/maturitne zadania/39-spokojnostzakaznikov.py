import tkinter

def uloha_39():
    nespokojni = [0] * 24
    celkovo_negativ = 0

    # Načítanie dát
    try:
        subor = open('38-spokojnost.txt', 'r', encoding='utf-8')
        for riadok in subor:
            if riadok.strip():
                cas, vyjadrenie = riadok.split()
                if vyjadrenie == 'nie':
                    hodina = int(cas.split(':')[0])
                    nespokojni[hodina] += 1
                    celkovo_negativ += 1
        subor.close()

        # Textové výstupy
        print(f"Celkový počet negatívnych vyjadrení: {celkovo_negativ}")

        max_nie = max(nespokojni)
        h_max_nie = nespokojni.index(max_nie)
        print(f"Najviac nespokojných: {max_nie} (v hodine {h_max_nie:02d})")

        print("\nPočty nespokojných v jednotlivých hodinách:")
        for h in range(24):
            if nespokojni[h] > 0:
                print(f"Hodina {h:02d}: {nespokojni[h]}x 'nie'")

        # Vykreslenie histogramu
        root = tkinter.Tk()
        root.title("Histogram nespokojnosti")
        canvas = tkinter.Canvas(root, width=480, height=520, bg='white')
        canvas.pack()

        sirka_stlpca = 480 // 24
        # Spodná hranica pre text (ponecháme miesto pre popis hodín)
        zakladna_y = 500 

        for h in range(24):
            x1 = h * sirka_stlpca
            # Výška stĺpca (mierku si určíme napr. 1 nespokojný = 5 pixelov)
            vyska = nespokojni[h] * 5 
            
            # Kreslenie stĺpca (červená farba pre nespokojnosť)
            canvas.create_rectangle(x1 + 2, zakladna_y - vyska, x1 + sirka_stlpca - 2, zakladna_y, fill='red')
            
            # Popis hodín pod osou X
            canvas.create_text(x1 + sirka_stlpca // 2, zakladna_y + 10, text=f"{h:02d}", font="Arial 8")

        root.mainloop()

    except FileNotFoundError:
        print("Súbor spokojnost_1.txt sa nenašiel.")

uloha_39()
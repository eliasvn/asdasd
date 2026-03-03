print("1: Yhteenlasku")
print("2: Vähennyslasku")
print("3: Kertolasku")
print("4: Jakolasku")
print("0: Lopeta ohjelma")

while True:
    valinta = input("Valitse 1-4 tai 0 lopettaaksesi ohjelman: ")

    if valinta == "0":
        break

    if valinta == "1" or valinta == "2" or valinta == "3" or valinta == "4":
        luku1 = float(input("Luku 1:"))
        luku2 = float(input("Luku 2:"))
        if valinta == "1":
            tulos = luku1 + luku2
            print(f"Tulos: {luku1} + {luku2} = {tulos}")

        elif valinta == "2":
            tulos = luku1 - luku2
            print(f"Tulos: {luku1} - {luku2} = {tulos}")

        elif valinta == "3":
            tulos = luku1 * luku2
            print(f"Tulos: {luku1} * {luku2} = {tulos}")

        elif valinta == "4":
            if luku2 != 0:
                tulos = luku1 / luku2
                print(f"Tulos: {luku1} / {luku2} = {tulos}")
            else:
                print("Virhe: Nollalla ei voi jakaa!")
    else:
        print("Virheellinen valina")
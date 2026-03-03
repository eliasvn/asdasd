syote = input("Anna luku (tyhjä lopettaa): ")

if syote != "":
    luku = float(syote)
    pienin = luku
    suurin = luku

    while True:
        syote = input("Anna luku (tyhjä lopettaa): ")

        if syote == "":
            break

        luku = float(syote)

        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku

    print(f"Pienin: {pienin}")
    print(f"Suurin: {suurin}")
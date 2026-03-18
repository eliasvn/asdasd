nimet = set()
while True:
    syote = input("Syötä nimi: ")
    if syote == "":
        break
    if syote in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(syote)

for nimi in nimet:
    print(nimi)
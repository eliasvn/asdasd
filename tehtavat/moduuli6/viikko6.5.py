def karsinta(lista):
    parilliset = []
    for luku in lista:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

numerot=[]

while True:
    syote = input("Syötä luku: ")
    if syote == "":
        break
    numerot.append(int(syote))
print(f"Raaka lista: {numerot}")
print(f"Karsittu lista (vain parilliset): {karsinta(numerot)}")

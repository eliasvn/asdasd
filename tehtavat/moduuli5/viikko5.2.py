syote = input("Syötä luku: ")
lista = []

while syote != "":
    luku = int(syote)
    lista.append(luku)
    syote = input("Syötä seuraava luku: ")


lista.sort(reverse=True)

print(*lista[:5], sep = ", ")




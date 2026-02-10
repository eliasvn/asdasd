luku = int(input("Syötä luku: "))

onko_alkuluku = "on alkuluku"

for jakaja in range(2, luku):
    if luku % jakaja == 0:
        onko_alkuluku = "ei ole alkuluku"
        break

print(f"Luku {luku} {onko_alkuluku}.")
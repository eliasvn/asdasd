import random

print("Arvaa luku 1-10")

vastaus = random.randint(1, 10)
arvaus = int(input("arvaus: "))

while arvaus != vastaus:
    if arvaus < vastaus:
        print("Liian pieni, kokeile uudestaan!")
    else:
        print("Liian suuri, kokeile uudestaan!")
    arvaus = int(input("arvaus: "))

print("Oikein!")

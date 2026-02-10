import random

arpakuutioiden_maara = int(input("Montako arpakuutiota heitetään?: "))

summa = 0

for i in range(arpakuutioiden_maara):
    x = random.randint(1, 6)
    print(x)
    summa = x + summa
print(f"Heittojen summa: {summa}")
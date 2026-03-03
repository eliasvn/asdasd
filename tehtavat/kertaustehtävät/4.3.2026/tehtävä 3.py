from math import sqrt

while True:
    syote = int(input("Syötä kokonaisulukuja: "))
    if syote < 0:
        print("Virheellinen numero.")
    elif syote == 0:
        break
    else:
        print(sqrt(syote))

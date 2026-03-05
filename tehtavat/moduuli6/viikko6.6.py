import math

def yksikkohinta(halkaisija, hinta):
    sade = (halkaisija/100) / 2
    pinta_ala = math.pi*sade**2
    return hinta / pinta_ala
x = 0
while x < 2:
    pizzan_halkaisija = int(input(f"Pizzan {x+1} halkaisija: "))
    pizzan_hinta = int(input(f"Pizzan {x+1} hinta: "))
    x = x + 1
print(yksikkohinta(pizzan_halkaisija, pizzan_hinta))
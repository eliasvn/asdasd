import math

def yksikkohinta(halkaisija, hinta):
    sade = (halkaisija/100) / 2
    pinta_ala = math.pi*sade**2
    return hinta / pinta_ala

pizzan1_halkaisija = float(input("Pizzan 1 halkaisija: "))
pizzan1_hinta = float(input("Pizzan 1 hinta: "))

pizzan2_halkaisija = float(input("Pizzan 2 halkaisija: "))
pizzan2_hinta = float(input("Pizzan 2 hinta: "))

yksikkohinta1 = yksikkohinta(pizzan1_halkaisija, pizzan1_hinta)
yksikkohinta2 = yksikkohinta(pizzan2_halkaisija, pizzan2_hinta)

if yksikkohinta1 < yksikkohinta2:
    print(f"Pizza 1 on parempi vastine rahalle ({round(yksikkohinta1,2)}€/m^2)")
elif yksikkohinta2 < yksikkohinta1:
    print(f"Pizza 2 on parempi vastine rahalle ({round(yksikkohinta2,2)}€/m^2)")
else:
    print("Molemmat pizzat ovat saman hintaisia per neliömetri.")
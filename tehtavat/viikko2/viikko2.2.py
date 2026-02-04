hytti_luokka = input("Mikä on hyttiluokkasi? (LUX/A/B/C): ").upper()

LUX_kuvaus = "LUX on parvekkeellinen hytti yläkannella."
A_kuvaus = "A on ikkunallinen hytti autokannen yläpuolella."
B_kuvaus = "B on ikkunaton hytti autokannen yläpuolella."
C_kuvaus = "C on ikkunaton hytti autokannen alapuolella."

if hytti_luokka == "LUX":
    print (LUX_kuvaus)
elif hytti_luokka == "A":
    print(A_kuvaus)
elif hytti_luokka == "B":
    print(B_kuvaus)
elif hytti_luokka == "C":
    print(C_kuvaus)
else:
    print("Virheellinen hyttiluokka.")

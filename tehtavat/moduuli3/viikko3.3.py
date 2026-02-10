sukupuoli = input("Syötä sukupuolesi (M/N): ").upper()
hemoglobiiniarvo = float(input("Hemoglobiiniarvosi (g/l): "))

if sukupuoli == "M":
    alaraja, ylaraja = 134, 195
elif sukupuoli == "N":
   alaraja, ylaraja = 117, 175
else:
    print("Virheellinen sukupuoli, kirjoita M tai N")

if hemoglobiiniarvo < alaraja:
    print("Hemoglobiiniarvosi on alhainen.")
elif hemoglobiiniarvo <= ylaraja:
    print("Hemoglobiiniarvosi on normaali")
else:
    print("Hemoglobiiniarvosi on korkea.")


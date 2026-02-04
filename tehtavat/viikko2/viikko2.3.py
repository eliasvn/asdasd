sukupuoli = input("Syötä sukupuolesi (M/N): ").capitalize()
hemoglobiiniarvo = float(input("Hemoglobiiniarvosi (g/l): "))


if sukupuoli == "M" and hemoglobiiniarvo < 117:
    print("Hemoglobiini arvosi on alhainen.")
    elif hemoglobiiniarvo > 37:

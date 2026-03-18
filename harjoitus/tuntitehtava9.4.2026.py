hedelmat = {
    "Kiivi" : "5€/kg",
    "Omena" : "2,50€/kg",
    "Vesimeloni" : "6€/kg"
}

while True:
    syote = input("hedelman nimi:").capitalize()
    if syote in hedelmat:
        print(hedelmat[syote])
    else:
        print("Virheellinen syöte")
        break

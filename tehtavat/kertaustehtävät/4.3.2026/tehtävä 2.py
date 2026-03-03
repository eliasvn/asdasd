tuntipalkka = float(input("Tuntipalkka: "))
tyotunnit = float(input("Tehdyt tunnit: "))
paiva = input("Viikonpäivä: ").capitalize()

if paiva == "Sunnuntai":
    paivapalkka = 2*tuntipalkka*tyotunnit

else:
    paivapalkka = tuntipalkka*tyotunnit

print(f"Päiväpalkka: {round(paivapalkka, 2)} euroa")

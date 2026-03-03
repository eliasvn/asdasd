nimi = input("Kerro nimesi: ").capitalize()
annos_hinta = 5.90

if nimi == "Matti":
    print("Seuraava, kiitos!")

else:
    syote = int(input("Montako keittoannosta? "))
    print(f"Kokonaishinta on {round(syote*annos_hinta,2)}")
    print("Seuraava, kiitos!")

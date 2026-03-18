lentoasema_lista = {
    "EFHK" : "Helsinki-Vantaa"
}

while True:
    print("1. Syötä uusi lentoasema")
    print("2. Hae jo syötetyn lentoaseman tiedot")
    print("3. Lopeta")
    syote = int(input("Valitse 1-3: "))

    if syote == 1:
        icao = input("Syötä lentoaseman ICAO-koodi: ")
        nimi = input("Syötä lentoaseman nimi: ").capitalize()
        lentoasema_lista[icao] = nimi
    if syote == 2:
        icao = input("Syötä lentoaseman ICAO-koodi: ")
        if icao in lentoasema_lista:
            print(f"Lentoasema ICAO-koodilla {icao} on {lentoasema_lista[icao]}")
        else:
            print("Lentoasemaa ei löytynyt.")

    if syote == 3:
        break

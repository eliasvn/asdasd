vuodenajat = ("talvi", "talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

kuukausi = int(input("Syötä kuukauden numero (1-12): "))

if 1 <= kuukausi <= 12:
    vastaus = vuodenajat[kuukausi]
    print(vastaus)
else:
    print("Virheellinen syöte")
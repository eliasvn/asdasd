vuosiluku = int(input("Vuosiluku: "))

if vuosiluku % 4 == 0 and vuosiluku % 100 != 0:
    print(vuosiluku, "on karkausvuosi.")
elif vuosiluku % 400 == 0:
    print(vuosiluku, "on karkausvuosi.")
else:
    print(vuosiluku, "ei ole karkausvuosi.")
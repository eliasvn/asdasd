username = "python"
password = "rules"
oikein=False
i=5

while i > 0:
    user_input = input("Syötä käyttäjänimi:")
    pass_input = input("Syötä salasana: ")

    if user_input == username and pass_input == password:
        oikein = True
        break
    else:
        i -= 1
        if i > 0:
            print(f"Kirjautumistiedot syötettiin väärin. {i} yritystä jäljellä")

if oikein == True:
    print("Tervetuloa!")
else:
    print("Pääsy evätty!")
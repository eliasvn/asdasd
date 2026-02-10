kaupungit =[]

for x in range(0, 5):
    x = input(f"Syötä kaupunki ({x+1}/5): ")
    kaupungit.append(x)

for kaupunki in kaupungit:
    print(kaupunki)



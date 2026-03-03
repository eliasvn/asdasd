tarina = []
while True:
    sana = input("Anna sana lisättäväksi tarinaan: ")
    if sana == "loppu":
        break
    if tarina and sana == tarina[-1]:
        break
    tarina.append(sana)
print(*tarina)
while True:
    bensiini_g = float(input("Montako nestegallonaa bensiiniä?: "))
    if bensiini_g < 0:
        break

def muunnos():
    bensiini_l = bensiini_g * 3.785
    return round(bensiini_l,2)
print(muunnos())




leiviska = float(input("Montako leiviskää: "))
naula = float(input("Montako naulaa: "))
luoti = float(input("Montako luotia: "))

leiviska_p = leiviska * 20 * 32 * 13.3
naula_p = naula * 32 * 13.3
luoti_p = luoti * 13.3

massa_grammoina = leiviska_p + naula_p + luoti_p

massa_kiloina = int(massa_grammoina // 1000)
grammat_loput = massa_grammoina % 1000

print("Massa nykymittojen mukaan: " , massa_kiloina , " kilogrammaa, " , round(grammat_loput, 2) , "grammaa")
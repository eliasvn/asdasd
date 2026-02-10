kuhan_pituus = float(input("Kuhan pituus senttimetreinä (esim. 28.5): "))

if kuhan_pituus < 37:
    print("Kuha on " + str(37-kuhan_pituus) + " senttimetriä alle sallitun pyyntimitan.")
    print("Laske kuha alas järveen.")
else:
    print("Kuha on sallitun mittainen.")

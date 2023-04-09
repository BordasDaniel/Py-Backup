pentek = [11, 19, 17]
szombat = [13, 22, 20]
vasarnap = [15, 30, 25]
hetfo = [7, 16, 15]

homersekletek = []
homersekletek = [pentek, szombat, vasarnap, hetfo]  # Ez is jó

print(homersekletek)


# Bejárható for ciklussal:
for nap in homersekletek:
    print(nap)

# Egyes elemei kiirásához két index segitségével tudunk.
# Először a lista indexe majd a lista elemének az indexe.
# Hogyha táblázat szerűen gondolunk a listára akkor először a sort kell megadni és azután az oszlopot
# 0-val kezdődik a sor és az oszlop is!
# Tehát 0. index és 2-es index

print(homersekletek[0][2])

"""
Hőmérséklet értékek 7:00, 15:00, 23:00 órakor.
"""

homersekletek = [[11, 19, 17], [13, 22, 20], [15, 30, 25], [7, 16, 15]]
print(homersekletek)
print(homersekletek[0])  # A 0. indexre hivatkozom amely egy lista.
print(homersekletek[0][2])  # A 0. indexű lista 2. indexű elemére hivatkozom.

for nap in homersekletek:
    print(nap)

# Egymás alá kiiratva a lista elemek
for nap in homersekletek:
    for meres in nap:
        print(meres)
    print('---------------')

# Módosithatjuk az értékeket.
homersekletek[0][2] = 29
print(homersekletek[0][2])

# Beszúrhatunk listákat.
homersekletek.insert(1, [0, 0, 0])
print(homersekletek)

# Egy beágyazott listákba való érték beszúrás.
homersekletek[0].insert(1, 0)
print(homersekletek)

# Egy adott elem törlése.
del homersekletek[0][0]
print(homersekletek)

# pop() metódussal.
# A pop metódus révén vissza is kapjuk a törölt értéket, van egy visszatérési érték
# Amelyet akár el is menthetünk egy változóban.
homersekletek[0].pop(0)
print(homersekletek)

x = homersekletek[0].pop(0)
print(homersekletek)
print(x)

# A korábban megismert lista metódusok szintén ugyanúgy működnek.
# Csak arra kell vigyázni hogy megfelelő módon hivatkozzunk az egyes elemekre.


# Eltérő hosszúságú beágyazott listák.

"""
Egy listában tárolt listák esetében természetesen az is megengedett, hogy a beágyazott listák eltérő hosszúságúak legyenek. 
Például egy napi hőmérsékleti adatokat tároló listában előfordulhat, hogy az egyik napon kevesebb adatot rögzítettek, a másikon többet.
"""
"""
[[11, 19],
 [13, 22, 20, 17, 16],
 [15, 30],
 [7, 16, 15, 11]] 
"""
homersekletek = [[11, 19], [13, 22, 20, 17, 16], [15, 30], [7, 16, 15, 11]]

"""
Ráadásul a változó elemszámú listák bejárása is ugyanolyan egyszerű for ciklus segítségével, mintha minden beágyazott lista azonos hosszúságú lenne.
"""

for x in homersekletek:
    for y in x:
        print(y)
    print('-------------')

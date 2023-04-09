szavak = []
szo = None

while szo != '':
    szo = input('Adj meg egy szót!\t')
    if szo != '':
        szavak.append(szo)

print('A listában lévő elemeid:\t', ('|').join(szavak))

#\t egy tabulátornyi távolság
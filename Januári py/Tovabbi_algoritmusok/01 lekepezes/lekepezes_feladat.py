rendszamok = ['ABC123', 'ABCD777', 'WN25L']

# 1. feladat

atalakitva = []

for szo in rendszamok:
    atmeneti = []
    for x in szo:
        if x.isalpha() == True:
            atmeneti.append('|')
        else:
            atmeneti.append('*')
    atalakitva.append(''.join(atmeneti))

print(atalakitva)

# 2. feladat


def fgv(szo):
    atmeneti = []
    for x in szo:
        if x.isalpha() == True:
            atmeneti.append('|')
        else:
            atmeneti.append('*')
    return ''.join(atmeneti)


uj = list(map(fgv, rendszamok))
print(uj)

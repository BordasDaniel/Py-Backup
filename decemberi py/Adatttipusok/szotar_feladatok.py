# 1. feladat.
"""

kutya = {'nev': input('Kérlek add meg a kutyád nevét!\t'),
         'eletkor': int(input('Kérlek add meg a kutyád életkorát!\t')),
         'ervenyes_oltas': bool(input('Kérlek add meg hogy van-e érvényes oltása a kutyádnak!\t'))}

# Vagy:
"""

"""
kutya = {}

kutya['nev'] = input('Kérlek add meg a kutyád nevét!\t')
kutya['eletkor'] = int(input('Kérlek add meg a kutyád életkorát!\t'))
kutya['ervenyes_oltas'] = bool(input('Kérlek add meg hogy van-e érvényes oltása a kutyádnak!\t'))
"""

"""

for x in kutya:
    print(x + ':', kutya[x])
    
"""
# 2. feladat.
"""
macska = {
    'nev': 'Cirmos',
    'kor': 5,
}
print(macska)
macska['nev'] = input('Mi legyen a cica új neve?\t')
macska['kor'] = int(input('Mi legyen a cica új kora?\t'))

for x in macska:
    print(x + ':', macska[x])
"""


# 3. feladat.
# NINCS KÉSZ

def kiiratas(diak):
    for x in diak:
        print(x + ':', diak[x])


def ertekadas(diak):
    kulcs = input('Add meg a kulcs nevét!\t')
    ertek = input('Add meg az értéket!\t')

    if kulcs == ertek:
        pass
    elif kulcs and ertek != "":
        diak[kulcs] = ertek
        kiiratas(diak)
        return kulcs, ertek
    else:
        print('Hiányos kulcspárat adtál meg!')
    kiiratas(diak)


diak = {
    'vezeteknev': 'Polgár',
    'keresztnev': 'Judit',
    'kor': 46,
    'magyar': True,
}

def egyenloseg(veg):
    for x in veg:
        if x == veg[0] and x == veg[1]:
            return True
        else:
            return False


def main():
    kiiratas(diak)
    print('---------------------')
    veg = (0, 1)
    allitas = egyenloseg(veg)
    while not allitas:
        veg = ertekadas(diak)
        print(veg)
        allitas = egyenloseg(veg)


main()

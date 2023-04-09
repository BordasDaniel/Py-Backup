'''
Az adatok beolvasása fájlból,
egy-egy sor az 'adatok' nevű lista egy-egy eleme
'''
adatok = []
with open('autok_listaja.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        # strip() metódus eltávolítja a sorvégi \n-t
        adatok.append(sor.strip())

'''
A 'autok' nevű lista 'auto' nevű szótár típusokat fog tartalmazni,
egy autó adatait egy szótár tárolja
'''
auto = {}  # egy auto adatai
autok = []  # szótárakat tartalmazó lista
for elem in adatok:
    auto_adatai = elem.split()
    auto['rendszam'] = auto_adatai[0]
    auto['marka'] = auto_adatai[1]
    auto['tipus'] = auto_adatai[2]
    auto['kor'] = int(auto_adatai[3])
    if auto_adatai[4] == '1':
        auto['javitva'] = True
    else:
        auto['javitva'] = False
    auto['koltseg'] = int(auto_adatai[5])

    autok.append(auto)
    auto = {}  # egy új, üres szótár objektum deklarálása ugyanazon a néven

print(autok)

'''
------------- 1. feladat -------------
A legöregebb autó: JTZ-774, Ford Fiesta, 25 éves.
'''
max_index = 0
oreg = autok[0]['kor']

for index, kocsi in enumerate(autok):
    if kocsi['kor'] > oreg:
        oreg = kocsi['kor']
        max_index = index

print(
    f"A legidősebb autó rendszáma: {autok[max_index]['rendszam']}, márkája: {autok[max_index]['marka']}, tipusa: {autok[max_index]['tipus']}, kora: {autok[max_index]['kor']}")

'''
------------- 2. feladat -------------
A már megjavított autók rendszáma:
TRU-234
OPO-223
ETW-231
SSA-772
GGT-434
'''
"""
for x in autok:
    if x['javitva']:
        print(x['rendszam'])
"""
lista = [print(x['rendszam']) for x in autok if x['javitva']]

'''
------------- 3. feladat -------------
Az egy autóra jutó átlagos javítási költség: 55425 Ft.
'''

osszeg = [x['koltseg'] for x in autok]
atlag = sum(osszeg) / len(osszeg)
print(int(atlag))

'''
------------- 4. feladat -------------
Adjon meg egy rendszámot (pl. ABC-123)!  SSA-772
A megadott rendszámú autó a műhelyben van.
'''


def keres():
    rendszam_keres = input('Adj meg egy rendszámot!\t')
    if not rendszam_keres in muhely:
        print(f'A(z) {rendszam_keres} rendszámú autó jelenleg nincs műhelyben.')
    else:
        print(f'A(z) {rendszam_keres} rendszámú autó jelenleg műhelyben van.')


muhely = [x['rendszam'] for x in autok if not x['javitva']]
print(muhely)
keres()

'''
------------- 5. feladat -------------
Adjon meg egy betűt!    X
A megadott betű az alábbi autók márka- vagy típusmegnevezésében fordul elő:
Ford C-Max
'''


def vizsgalat(autok,betu):
    for x in autok:
        if betu.lower() in x['marka'] or betu.upper() in x['marka']:
            print(x['marka'], x['tipus'])
        elif betu.lower() in x['tipus'] or betu.upper() in x['tipus']:
            print(x['marka'], x['tipus'])


betu = input('Kérlek adj meg egy betűt!\t')
vizsgalat(autok, betu)


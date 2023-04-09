adatok = []
with open('diak_adatok.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        # print(sor.strip()) #Egymás alá kiirva a fájl tartalma.
# A .strip() metódus segitéségvel szabadulunk meg a különböző karakterektől
# Vagy opcionálisan megadott karaktereket, vagy alapértelmezettként ezeket a wildspace karaktereket
# Space vagy például a sorvégi enter
        adatok.append(sor.strip()) # Lista feltöltése adatokkal.


print(adatok)
diak = {}
diakok = []

for elem in adatok:
    diak_adatok = elem.split() # Ez alapértelmezettként ha nem adunk meg argumentumot akkor a specek mentén darabolja fel a stringet.
    # print(diak_adatok)
    diak['vezeteknev'] = diak_adatok[0]
    diak['keresztnev'] = diak_adatok[1]
    diak['kor'] = int(diak_adatok[2])
    diak['osztaly'] = diak_adatok[3]
    if diak_adatok[4] == '1':
        diak['kollegista'] = True
    else:
        diak['kollegista'] = False
    diakok.append(diak)
    diak = {}

print(diakok)

# 1. feladat
"""
10.A osztályos tanulok neveinek kiiratása
"""
print('\n---------------> 1. feladat <---------------')
print('10. A osztályos diákok:')


for diak in diakok:
    if diak['osztaly'] == '10.A':
        print(diak['vezeteknev'] + ' ' + diak['keresztnev'])


# 2. feladat
"""
10. B osztályos tanulók kigyűjtése listába
"""
print('\n---------------> 2. feladat <---------------')
print('10. B osztályos diákok listában:')

"""
tizedik_b = [diak['vezeteknev'] + ' ' + diak['keresztnev'] for diak in diakok if diak['osztaly'] == '10.B']
print(tizedik_b)
"""

"""
for diak in diakok:
    if diak['osztaly'] == '10.B':
       tizedik_b.append(diak['vezeteknev'] + ' ' + diak['keresztnev'])
print(tizedik_b)
"""


tizedik_b = [diak for diak in diakok if diak['osztaly'] == '10.B']
print(tizedik_b)


# 3. feladat
"""
diákok életkorának az átlaga
"""
print('\n---------------> 3. feladat <---------------')

osszeg = [kor['kor'] for kor in diakok]
print(int(sum(osszeg)/len(osszeg)))
print(osszeg)

osszeg = 0
for diak in diakok:
    osszeg += diak['kor']
atlag = osszeg/ len(diakok)
print(f'A diákok átlag életkora: {atlag:.2f}')


# 4. feladat
"""
(egyik legidősebb diák nevének és korának kiirása
"""
print('\n---------------> 4. feladat <---------------')


max_index = 0
max_kor = diakok[0]['kor']

for index, diak in enumerate(diakok):
    if diak['kor'] > max_kor:
        max_kor = diak['kor']
        max_index = index

print(f"A legidősebb diák kora: {max_kor}, neve: {diakok[max_index]['vezeteknev']} {diakok[max_index]['keresztnev']}")

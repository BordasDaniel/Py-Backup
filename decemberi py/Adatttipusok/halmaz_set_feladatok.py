# 1. feladat.
# y = 2x+3 és y=3x+1
"""
x = set()
ertel_tartomany = [x.add(szam) for szam in range(0, 10)]
print(f'Értelmezési tartomány: {x}')

ertekkeszlet = set()
y = [ertekkeszlet.add(2*x+3) for x in x]
print(f'Az y = 2x+3 értékkészlete: {ertekkeszlet}')

ertekkeszlet_02 = set()
y_02 = [ertekkeszlet_02.add(3*x+1) for x in x]
print(f'Az y = 3x+1 értékkészlete: {ertekkeszlet_02}')

print(f' A két halmaz uniója: {ertekkeszlet | ertekkeszlet_02}')
print(f' A két halmaz metszete: {ertekkeszlet & ertekkeszlet_02}')
print(f' A két halmaz különbsége: {ertekkeszlet - ertekkeszlet_02}')
"""
# 2. feladat.
"""
import random


def kitalalando(szamok):
    for szam in range(5):
        szamok.add(random.randint(1, 10))
    print(szamok)


def jatekos_tippjei(jatekos):
    for tipp in range(5):
        jatekos.add(int(input('Add meg a számot amire gondoltál!\t')))


def ha_talal(talalat, nem_talalt, jatekos, szamok):
    metszet = jatekos & szamok
    if not len(metszet) == 0:
        talalat.update(metszet)
        print(f'Gratulálok eltaláltál: {len(metszet)} darab számot \n A számok amelyeket eltaláltál: {metszet}')
    else:
        nem_talalt.update(metszet)
        print('Sajnos nem találtál el egyetlen számot sem')


def rogzit(jatekos, szamok):
    print(f'A számok amelyek rögzitésre kerültek a játék során: {jatekos | szamok}')
    print(f'A számok amelyek a játék során nem szerepeltek: {szamok - jatekos}')


def main():
    szamok = set()
    jatekos = set()
    talalat = set()
    nem_talalt = set()
    kitalalando(szamok)
    jatekos_tippjei(jatekos)
    ha_talal(talalat, nem_talalt, jatekos, szamok)
    rogzit(jatekos, szamok)


main()
"""

# 3. feladat:

Peti_kedvencei = {'halászlé', 'bécsi szelet', 'bukta', 'rakott krumpli', 'almás rétes' }
Kriszti_kedvencei = {'borsóleves', 'bécsi szelet', 'túrós tészta', 'lecsó', 'almás rétes' }

mindketten = Peti_kedvencei & Kriszti_kedvencei
print(f'Mindketten szeretnek {len(mindketten)} darab fajta ételt. \n Ezek a: {mindketten}.')

Peti_etelei = Peti_kedvencei - Kriszti_kedvencei
print(f'Peti {len(Peti_etelei)} fajta ételt szeret amelyet Kriszti nem. \n Ezek a: {Peti_etelei}')

Kriszti_etelei = Kriszti_kedvencei - Peti_kedvencei
print(f'Ételek amelyeket csak az egyikük szeret:\n Peti ételei: {Peti_etelei} \n Kriszti ételei: {Kriszti_etelei}.')

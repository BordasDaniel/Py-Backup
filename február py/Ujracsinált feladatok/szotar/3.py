"""
3.1: 
Írj egy programot, amely szótárban tárol adatokat (legalább egy int, str, és bool típusút). 
A program a írja ki a képernyőre az adatszerkezet! A felhasználónak legyen lehetősége ezt az adatszerkezetet egy kulcs-érték párral bővítenie.
A program végül írja ki a képernyőre a frissített adatszerkezetet!
"""

"""
3.2:
Módosítsd úgy a programot, hogy a felhasználónak többször is legyen lehetősége bővíteni az adatszerkezetet!
"""



def bevitel(cica):
    adat_neve = input('Mi az adat neve?\t')
    cica[adat_neve] = input('Mi az adatod tartalma?\t')
    return cica

def kiirat(cica):
    for x in cica:
        print(x, cica[x])


def adat():
    cica = {
        'nev': 'Cirmi',
        'kor': 6,
        'oltas': True
    }
    return cica


def amig(cica):
    while (user := input('Szeretnél hozzáadni adatot?\t')) == "True":
        bevitel(cica)
        kiirat(cica)

def main():
    cica = adat()
    kiirat(cica)
    amig(cica)
main()
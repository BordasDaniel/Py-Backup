# 1. feladat.
"""
import random

lista = []

for y in range(4):
    lista.insert(0, [])
    for x in range(3):
        lista[0].append(random.randint(0, 25))

print(lista)
"""
import random

# 2. feladat.
# NINCS KÉSZ
"""
def elhelyez(tarolo, jel):
    for y in range(3):
        tarolo.insert(0, [])
        for x in range(3):
            tarolo[0].append(jel)


def harmas(tarolo):
    for x in tarolo:
        print(" ".join(x))


def felulir(tarolo, adat):
    tarolo[adat[0]][adat[1]] = '+'



def koodinata():
    a = int(input('Adj meg egy koordinátát!\t'))
    b = int(input('Adj meg egy koordinátát!\t'))
    return a, b


def iras_jel():
    return input('Add meg milyen jellel irjon!\t')



def main():
    jel = iras_jel()
    while not any(adat := koodinata()) > 2:
        try:
            tarolo = []
            elhelyez(tarolo, jel)
            felulir(tarolo, adat)
            harmas(tarolo)
        except:
            print('Túl nagy értéket adtál meg!')
            exit()


main()"""

# 3. feladat.


def uj_lista(lista):
    for y in range(5):
        lista.insert(0, [])
        for x in range(3):
            lista[0].append(random.randint(-5, 5))


def ujat(nem_negativ):
    nem_negativ.append([])


def valogat(veletlen):
    index1 = 0
    nem_negativ = []
    for x in range(5):
        # ujat(nem_negativ)
        elsok = lambda nem_negativ: nem_negativ.append([])
        elsok(nem_negativ)
        for y in veletlen[index1]:
            if y >= 0:
                nem_negativ[index1].append(y)
        index1 += 1
    return nem_negativ


def main():
    veletlen = []
    uj_lista(veletlen)
    print(veletlen)
    nem_negativ = valogat(veletlen)
    print(nem_negativ)


main()

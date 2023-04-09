import random


def szotarozas(szotar, lista):
    for x in lista:
        szotar[x] = 0


def beosztas(kiosztas):
    for index, ember in enumerate(kiosztas):
        print(f'{index}. napon {ember}')


def osszesites(szotar, kiosztas):
    for x in kiosztas:
        szotar[x] = kiosztas.count(x)
    print(szotar)


szotar = {}
lista = ['Barabás','Kolnay','Csele','Leszik','Richter','Nemecsek']
nap = int(input('Hány napig tartson?\t'))
kiosztas = [random.choice(lista) for x in range(nap)]

szotarozas(szotar, lista)
beosztas(kiosztas)
osszesites(szotar, kiosztas)

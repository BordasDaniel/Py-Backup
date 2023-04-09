import random

#1. feladat:

'''
def main():
    szam = random.randint(1,10)
    return szam
    

def valtozik():
    global beker
    beker = int(input('Adj meg egy számot!'))
    return beker
         

szam = main()
print(szam)
beker = None
while beker != 0:
    szam = valtozik()
    print(szam)
    '''


#2. feladat:

def main(list):
    ['a','b','c']
    print(list)


def masik():
    lista = [input('Adj meg egy betüt\t') for x in range(3)]
    return lista


def amig(lista):
    while not all(x == lista[0] for x in lista):
    # while all(x == new_list[0] for x in new_list) == False:
        lista = masik()
        main(lista)
    # while new_list[0] != new_list[1] != new_list[2]:
    #     new_list = masik()
    #     main(new_list)


new_list = [0,1,2]
amig(new_list)


# 3. feladat:
# Külön otbetus.py fájlban.


# 1. újra

'''
def main():
    return random.randint(1,10)
    
def amig(szam):
    while szam != 0:
        szam = valtozik()
        print(szam)
    


def valtozik():
    return int(input('Adj meg egy számot!'))


szam = main()
print(szam)
amig(szam)
'''


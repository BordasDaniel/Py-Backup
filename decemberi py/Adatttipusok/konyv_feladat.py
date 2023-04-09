
def beker(konyv):
    konyv['szerzo'] = input('Add meg a könyv szerzőjét!\t')
    konyv['cim'] = input('Add meg a könyv cimét!\t')
    if konyv['szerzo'] == '' or konyv['cim'] == '':
        exit()


def berak(konyv, osszes_konyv):
    osszes_konyv.append(konyv.copy())


def szepites(osszes_konyv):
    for x in osszes_konyv:
        print(x)


def main(konyv, osszes_konyv):
    while True:
        beker(konyv)
        berak(konyv, osszes_konyv)
        szepites(osszes_konyv)


osszes_konyv = []
konyv = {}

main(konyv, osszes_konyv)
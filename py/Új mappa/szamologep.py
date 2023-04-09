def elso():
            print('Az első opciót választottad')
            time.sleep(1.75)
            osszead()

def masodik():
            print('A második opciót választottad')
            time.sleep(1.75)
            osztas()
            time.sleep(1.5)

def harmadik():
            print('A harmadik opciót választottad')
            time.sleep(1.75)
            szoroz()
            time.sleep(1.5)

def valasz():
    time.sleep(1.5)
    print('\t\t\t\t\t       Válassz a lehetőségek közül:')
    print('\t\t\t\t\t1. Öszeadás/Kivonás','2. Osztás','3. Szorzás', sep=' | ', end=' ' and '\n',)
    szam = input('Adj meg egy számot!\t')
    return szam


def osszead():
    mennyi = int(input('Mennyi számot szeretnél összeadni?\t'))
    lett = 0
    for x in range(mennyi):
        szam = int(input('Add meg a számot!\t'))
        lett += szam
        print('Eddig: ',lett)
    print('Végül a számod: ',lett)
    time.sleep(1.5)


def szoroz():
    mennyi = int(input('Mennyi számot szeretnél összeszorozni?\t'))
    lett = 1
    for x in range(mennyi):
        szam = int(input('Add meg a számot!\t'))
        lett *= szam
        print('Eddig: ',lett)
    print('Végül a számod: ',lett)
    time.sleep(1.5)


def osztas():
    mennyi = 0
    while not mennyi >= 2:
        mennyi = int(input('Mennyi számot szeretnél elosztani? (Minimum 2)\t'))

    lista = [int(input('Add meg a számot!\t')) for x in range(mennyi)]
    while not len(lista) == 1:
        szam = lista[0] / lista[1]
        lista[0] = szam
        lista.remove(lista[1])
    print(szam)




import time

print('Üdvözöllek a programomban!','Kérlek válassz opciót!','Ha kiszeretnél lépni üss egy x-et!',sep='\n')
while True:
    bevitel = valasz()
    if bevitel == 'X' or bevitel == 'x':
        print('Viszlát!')
        exit()
    else:
        if bevitel == str(1):
            elso()
        elif bevitel == str(2):
            masodik()
        elif bevitel == str(3):
            harmadik()
        else:
            print('\tHIBÁS ÉRTÉK')
            time.sleep(1.75)
        
        
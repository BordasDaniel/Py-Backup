#1. feladat
#NEM KÖSZÖNÖM NEM FOGOK RAJZOLNI

'''
def szoveg(text):
    print(text)

text = input('Adj meg valamit\t')
szoveg(text)
'''
#2. feladat
'''
def szamok(x):
    if x > 0:
        print('A szám pozitiv')
    elif x < 0:
        print('A szám negativ')
    else:
        print('A szám 0')

x = int(input('Adj meg egy számot\t'))

szamok(x)
'''

#3. feladat
'''
x = int(input('Adj meg egy számot!\t'))
y = int(input('Adj meg egy számot!\t'))

def hasonlit(x,y):
    if x > y:
        print(x, 'nagyobb')
    elif y > x:
        print(y, 'nagyobb')
    else:
        print('A két szám értéke egyenlő')

hasonlit(x,y)
'''

#4. feladat

lista = [input('Adj meg vmit\t') for x in range(3)]

szo = lista[0]

def eljaras(lista,szo):
    for x in lista:
        if len(szo) > len(x):
            szo = x
    print(szo)
eljaras(lista,szo)


#5.1 és 5.2 feladatra ugyan az vonatkozik mint az 1.-re
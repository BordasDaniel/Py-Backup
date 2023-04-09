'''
lista = []
harom = 0
allitas = bool

for i in range(3):
    szam = int(input('Adj meg egy számot!\t'))
    lista.append(szam)

for x in lista:
    if x %3==0:
        harom +=1

if harom == 3:
    allitas = True
else:
    allitas = False
print(allitas)
print(lista)
'''

'''
szam = int(input('Adj meg egy számot!\t'))
lista = [x for x in range(0,szam) if x %3 == 0]
print(lista)
'''

'''
lista = []

for x in range(2):
    szam = int(input('Adj meg egy számot!\t'))
    lista.append(szam)

szam = [print(x) for x in range(lista[0],lista[1]+1)]
print(lista)
'''


'''
szam = int(input('Adj meg egy számot!\t'))
print(' '*szam,'START')
'''


'''
szam = int(input('Adj meg egy számot!\t'))
lista = [x for x in range(0,szam)]
print(lista)
print(sum(lista))
'''

'''
x = input('Adj meg egy szót!:\t')

for i in x:
    print(i,sep='\n')
'''
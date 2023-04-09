import random

'''
lista = [random.randint(1,5) for x in range(5)]
paros = [y for y in lista if y%2==0]
print(paros, lista)
print(sum(paros))

'''
'''
szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']
ujak = [x for x in szavak if x.startswith('a') or x.startswith('A')]
print(ujak)
'''

'''
szavak = ['Elemér', 'Emma', 'ajtó', 'róka', 'egér']
lista = [x for x in szavak if 'e' in x  or 'E' in x]
print(lista,len(lista),'darab')
'''


#A SZÁMLÁLÁS esetében azt vizsgáljuk, hogy egy bizonyos tulajdonságú elemből 
#hány darab van az adatsorban (itt a listában).
#A program azt vizsgálja, hogy hány darab hárommal osztható szám van a listában.
'''
lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

darab = 0
for szam in lista:
	if szam % 3 == 0:
		darab = darab + 1

print('A listában lévő hárommal osztható számok száma: ', darab)  
'''



szavak = ['Elemér','tó','ajtó','róka','egér','Aladár','pingvin']
# lista = [x for x in szavak if len(x) > 4]
# print(lista,len(lista))

darab = 0
for x in szavak:
    if len(x) > 4:
        darab +=1
print(darab)

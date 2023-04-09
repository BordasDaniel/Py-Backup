ertekek = ['1','2','3','4']
#Stringből int a map() függvény segitségével
#A map() függvény egy magasabb rendű függvény.
#A map() függvény argumentumként átvesz egy függvényt és átvesz egy bejárható tárolót pl.: egy listát

print(list(map(int, ertekek)))
szamok = list(map(int, ertekek))
print(szamok)
jel = ([int(x) for x in ertekek])
print(type(jel[0]))


lista = ('1','2','3')
print(tuple(map(int, lista)))

allatok = ['kutya','macska','egér']

print(list(map(lambda allat: allat.upper(), allatok)))
print([allat.upper() for allat in allatok]) #Lista értelmezéssel (list comprehension)

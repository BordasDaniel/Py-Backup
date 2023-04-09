'''
szamok = [12,5,4,8,9,5,-2,11,10,12,6]
min = szamok[0]
max = szamok[0]

for x in szamok:
    if x < min:
        min = x
    if x > max:
        max = x

print(min)
print(max)
'''
'''
szavak = ['Elemér','tó','ajtó','róka','egér','Aladár','pingvin']

rövid = szavak[0]
hosszabb = szavak[0]

for y in szavak:
    if len(rövid) > len(y):
        rövid = y
    if len(hosszabb) < len(y):
        hosszabb = y

print(rövid)
print(hosszabb)
'''

#Szélsőérték meghatározás beépített függvénnyel
#Pythonban létezik a min() és max() beépített függvény, amely a paraméterként megadott értékek közül a legkisebb, ill. legnagyobb értékkel tér vissza. Paraméterként fogadhat összetett adattípust, pl. listát is.

print(max(17, 95, -2, 0, 34, 19)) #95
print(min(17, 95, -2, 0, 34, 19)) #-2
    
szamok = [17, 95, -2, 0, 34, 19]
print(max(szamok)) #95
print(min(szamok)) #-2
  
#Ha sztringeket adunk meg, akkor az ABC sorrend számít, tehát a max() esetében az ABC sorrendben legutoljára szereplő sztringgel tér vissza.

print(max('szilva', 'eper', 'barack', 'banán')) #szilva
print(min('szilva', 'eper', 'barack', 'banán')) #banán
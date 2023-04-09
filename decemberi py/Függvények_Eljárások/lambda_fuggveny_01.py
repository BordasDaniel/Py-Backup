szamok = [7,2,12,-9]
print(sorted(szamok)) #Rendezés
print(sorted(szamok, reverse=True)) #Forditott rendezés
print(sorted(szamok, key=abs ,reverse=True)) #A key helyére egy függvény referencia kerül. Az abs függvény abszólút értéket jelent emiatt kerül a -9 az 1. indexre mivel -9 abs értéke 9
print(sorted(szamok, key=abs)) #Reverse nélkül, alapból az értéke False mikor nincs beirva.
'''
A sorted egy úgynevezett magasabb rendű függvény. A magasabb rendű függvények más függvényekkel együtt működnek.
Ez azt jelenti hogy vagy függvényeket vesznek át paraméterként vagy függvényekkel térnek vissza ebben az esetben ugye a sorted
paraméterként veszi át az abszolút érték függvényt. A függvénynek csak a referenciáját kell megadni tehát az abs után nem irhatunk zárójelet
pl print(sorted(szamok, key=abs())) mert ez a függvénynek a hivását jelentené erre itt most nem kell hogy sor kerüljön hogyha igy futtatnánk a scriptet
akkor hibát eredményezne. Tehát fontos az hogy paraméterként a függvénynek csak a nevét, a referenciáját kell átadni és akkor működik.
Más magasabb rendű függvények pl.: min(), max(), sort(), sorted()
'''

#https://realpython.com/python-lambda/
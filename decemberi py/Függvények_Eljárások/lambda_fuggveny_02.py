def b_oldal(teglalap):
    return teglalap[1]


teglalapok = [[1, 9], [2, 3],[5, 7]] #Beágyazott listák vagy más néven 2 dimenziás listák

print(max(teglalapok)) #Az [5, 7] lesz mivel a beágyozott listáknak az 1. elemeit hasonlitja össze.
print(max(teglalapok, key=b_oldal)) #Nem csak a python által beépitett függvények használhatók hanem mi is csinálhatunk egyet.
print(max(teglalapok, key=lambda teglalap: teglalap[1])) #Ez egy egyszeri használatos névtelen függvény amelyet helyben irunk meg, úgynevezett lambda függvény.
#Használata key=lambda majd az argumentum(jelenleg ez teglalap) aztán egy : és utána irhatunk egy egyszerű kifejezést és nem kell return, nem kell elnevezni
#argumentum : Teljesen mindegy mi a név ezt mi választjuk meg. Arról van szó hogy itt bejárásra kerül az általunk átadott lista és annak az elemei jelennek majd meg itt majd bemeneti értékként
#tehát argumentumként

#Összefoglalva lambda függvény:
'''
-névtelen kis függvények
-tetszőleges számú argumentum
-egyetlen egy kifejezés visszatéréi értékként.
'''

print(min(teglalapok, key=lambda tl: tl[0] * tl[1] )) #Megkeresi a legkissebb értékét az a és b szorzatai közül.
print(min(teglalapok, key=lambda tl: (tl[0] + tl[1])*2)) #Megkeresi a legkisebb kerületet.

tl_kerulet = lambda tl: (tl[0] + tl[1])*2 #Megtehetó habár inkább kerülendő mivel a python irányelvei ellen megy, ugyanis elnevezünk egy névtelen függvényt. Inkább használjuk def-et.
print(min(teglalapok, key=tl_kerulet))


#Több argumemtum esetébem vesszővel választjuk el egymástól őket és itt sem szabad használni a kerek zárójelet hanem csak vesszővel elválasztva felsorolojuk ezeket az argumentumokat a kettőspont elött.
koszont = lambda vezeteknev, keresztnev: f'Szia {vezeteknev} {keresztnev}!'
print(koszont('Kis','Péter'))

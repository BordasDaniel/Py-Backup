#Vizsgálat int tipussal

def fgv_1(x):
    x +=1


szam = 300
print(f'A függvényhívás elött: {szam=}')
fgv_1(szam)
print(f'A függvényhívás után: {szam=}')


#Vizsgálat list tipussal

def fgv_2(x):
    x[0] += 17

szamok = [1,2,3,4]
print(f'A függvényhívás elött: {szamok=}')
fgv_2(szamok)
print(f'A függvényhívás után: {szamok=}')

#Magyarázat:
'''
Amikor az ötös sorban létrejön az értékadás akkor létrejön egy objektum illetve egy arra mutató referencia is létrejön.
Amikor pedig a hetes sorban meghivjuk a függvényt akkor ennek az objekumnak a referenciáját adjuk át a függvény számára és mostmár az x is erre az objektumra mutat.
A második sorban megakarjuk növelni a 300 értékét eggyel, viszont az int tipusu objektum megváltoztathatatlan igy aztán amikor amikor értéket növelünk egy új objektumot hozunk létre.
És ezután már az x erre az újonnan létrejött objektumra fog mutatni.
Amikor pedig a vezérlés vissza kerül a programba akkor gyakorlatilag az x nevű változó is megszűnik és mivel ez mutatott a 301-es értéket tároló objektumra erre sincs már szükség igy ezek eltünnek.
A memóriáknak ezáltal foglalt területe felszabaditható és igy aztán nem meglepő amikor a szám nevű változóban tárolt értéket iratjuk ki a képernyőre akkor 300 fog megjelenni.
'''

#Megoldás:
'''
Ha a függvény segitségével szeretnénk növelni a számban tárolt értéket akkor másképp kell eljárni. Egy return utasitással vissza kell tériteni az értéket.
'''

def fgv_3(x):
    x+=1
    return x

szam = 300
print(f'A függvényhívás elött: {szam=}')
szam = fgv_3(szam) #Ez már egy új objektum ugyanis a szám már a 301-es értéket tartalmazó objektumra mutat.
print(f'A függvényhívás után: {szam=}')


#Ebben az esetben mind a főprogram mind a függvény ugyanazzal az objektummal dolgozik.
def fgv_4(x):
    x[0] +=17


szamok = [1,2,3,4]
print(f'A függvényhívás elött: {szamok=}')
fgv_4(szamok)
print(f'A függvényhívás után: {szamok=}')

# Magyarázat:
'''
A 15. sorban történő értékadás hatására létrejön egy lista objektum amire mutat a számok nevű referencia.
És amikor a 17. sorban meghivjuk a függvényt akkor átadásra kerül ennek az objektumnak a referenciája igy aztán már a 11. sorban létrejövő x változó referencia, pointer
ugyan úgy arra az objektumra mutat ami a 15. sornak a hatására létrejött amikor pedig a 12. sorban megváltoztatjuk a 0. indexű elem értékét megnöveljük 17-tel akkor egyszerűen megváltozik
az objektumban tárolt érték, de marad ugyanaz az objektum nem fog új objektum keletkezni igy aztán nem is kell igazán a függvényből bármivel is visszatérnünk felesleges lenne ebben az esetben a return utasitás
hiszen amikor a vezérlés visszakerül a 18. sorra akkor ugye megszűnik az x lokális változó, de erre az objektumra ami ugyebár tárolja a listánkat mutat egy másik referencia is, a számok is.
Ezt az objektumot továbbra is elérjük mostmár ezt a megváltozott tartalmú objektumot is a számok referenciával és igy aztán dolgozhatunk ezzel a változó névvel a főprogramunkban a továbbiakban.
'''


def teglalap_novel(a,b):
    a *=2
    b *=2
    return a,b

a_oldal = 3
b_oldal = 9
# a_oldal,b_oldal = teglalap_novel(a_oldal,b_oldal) #Az értékek frissülnek egy kicsomagolt tuple jön létre.
# print(a_oldal,b_oldal)
visszateresi_ertek = teglalap_novel(a_oldal,b_oldal)
print(visszateresi_ertek)
print(type(visszateresi_ertek))

            #Local (function scope)
'''
def negyzet(a):
    print(a)
    return a**2

print(negyzet(3))
print(a) #Az a nevű változó egy lokális változó emiatt a függvényen kivül nem lehet meghivni mivel nem létezik.
'''


            #Global (module) scope
#Egy globális változóhoz hozzáférhetünk bárhol akár a függvényen belül is, de az értékét megváltoztatni nem tudjuk benne.


'''
def negyzet(a):
    #szam = 2 Ezt az értéket kellene megani például hogy müködjön.
    #szam +=1 
    #Hiba üzenet mivel ebben az esetben létrejött egy szam nevü váltózó lokálisan is, és nem müködik mivel nem felel meg a feltételnek ugyanis nincs alap értéke.
    print(f'A függvényen belül: {szam}')
    return a**2

szam = 17 #Globális változó emiatt a program minden pontján elérhetó, akár a függvényen belül is.

print(f'A függvényen kivül: {szam}')
negyzet(3)
'''

#----------------------#
'''
def negyzet(a):
    print(f'A negyzet függvényen belül: {a}')
    return a**2


def kob(a):
    print(f'A kob függvényen belül: {a}')
    return a**3

a = 0
print(f'A függvényen belül: {a}')
print(negyzet(3))
print(kob(3))
'''
#----------------------#

'''
def negyzet(a):
    szam = 10
    print(f'A negyzeten belül: {szam}')
    return a**2
print(negyzet(2))
'''

#----------------------#
            #Függvényen belül létrehozott globális változó
#Egy külön sorba a global kulcsszó és a váltózó nevét kell megadni hozzá
#Viszont ezt próbáljuk meg kerülni mivel akkor a függvényét lényegét avagy a függvény elkülönitése már nem lesz lehetséges.

'''
def negyzet(a):
    global szam
    szam = 10
    print(f'A negyzeten belül: {szam}')
    return a**2
print(negyzet(2))
print(f'A függvényen kivül: {szam}')
'''

            #Enclosing (nonlocal) scope
#A belső függvényből elérhető a külső változót.
#Mert mikor meghivod a kulso függvényt létrejön egy lokális változó amely a kulso és belső függvényen belül él ameddig vissza nem térsz.
#Tehét amikor sor kerül a belso függvény hivására akkor a szam nevü változó még él és ezért a belső függvényből is hozzáférünk.
#Bármilyen mélyen beágyazott függvényen belül is lehetséges ez és amikor visszatérünk a külső függvényből akkor szűnik meg a szam nevű változó és onnantól kezdve már nem hivatkozhatsz rá a függvényen kivül.


'''
def kulso_fgv():
    szam = 17

    def belso_fgv():
        print(f'A belső függvényből {szam}')
    
    belso_fgv()

kulso_fgv()
'''


            #Built-in scope

#dir() megjeleniti az összes program futása során létező objektumunknak az attributumát illetve a metődusait.
'''
print(dir())
print('--------------------------')
print(dir(__builtins__)) #Ezek a beépitett nevek.
print(len(dir(__builtins__)))
'''


#-----------------------------------------
#Main függvény a pythonban
#Szépen és világosan elvannak különitve az egyes váltózók mindegyiknek megvan a maga scopeja, a tér része ahol látható
#és hogyha valamit át szeretnénk adni egy másik függvénynek arról nekünk magunknak programozóknak kell gondoskodni és igy aztán
#megmarad a függvényünknek felhasználhatósága, az a fajta elv hogy a függvényünknek a működése csakis kizárólag
#a paramétertől a bemenettől függ.

def negyzet(a):
    return a**2

def main():
    szam = 17
    print(negyzet(2))

main()
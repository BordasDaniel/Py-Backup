# Ctrl + Shift + i a lehetséges paramétereknek a listája
# Szintén Ctrl + Shift + i-vel lehet editelni a fájlt a pythonban fájlban ha ráhúzod az egeret.


# forrasfajl = open('szamozott_sorok.txt')

# Ha nem ugyan abban a mappában van a fájl a két fájl
# Akkor ki nem elég csak a fájlnevét megadni hanem ki kell egésziteni az elérési útvonallal is
# Ebben az esetben egy almappáról van szó
# Arra a könyvtárra, a könyvtár struktúrának arra a szintjére ahol most ez a .py fájl van
# Egy ponttal és egy perjellel tudok hivatkozni. Ezen belül található az adatok nevű almappa.
# És ezen belül pedig elhelyezkedik a szamozott_sorok.txt nevű fájl

forrasfajl = open('./adatok/szamozott_sorok.txt')


# Objektum képességei, tulajdonságai
print(dir(forrasfajl))
print(help(forrasfajl)) # Ez részletesebb

# Az is előfordulhat az elérési útvonal esetében a könyvtár struktúrában felfelé kell lépni
# Ilyenkor először hivatkozuk a könyvtár aktuális pozicójára utána pedig két pontot kell adni
# És akkor ott már egy szintel feljebb kerülök és itt eltudom érni a szamozott_sorok.txt-t
# Tehát a két ponttal tudok felfelé lépni

# open('./../szamozott_sorok.txt')

# Ha a fájlnak a nevét vagy a kiterjesztési útvonalát rosszul adjuk meg
# FileNotFoundError-t fogunk kapni tehát ilyen fájlt vagy könyvtárat nem talál
# Ebben az esetben megszakad a programnak a futása.

# forrasfajl = open('./adatok/amozot_soro.tx')

# A probléma elkerülése érdekében a kivétel kezelés fog segiteni
# A kivétel kezelés alternativájaként megtehetjük azt is hogy a fájl megnyitása elött ellenőrozzük hogy egyáltalán
# Létezik-e, elérhető-e az adott fájl, ehhez szükségünk lesz az os modulra

import os

if os.path.exists('adatok/amozot_soro.tx'):  # True értékkel tér visza hogyha a fájl elérhető
    forrasfajl = open('adatok/amozot_soro.tx')


# Az első lépés a fájlnak a megnyitása, a fájl objektumnak elkészitése.
# Utána jöhetnek a fájlhoz kapcsolódó műveletek (ebben az esetben az adatbeolvasás)
# És amiről nem szabad megfeledkezni az pedig a fájlnak a bezárása.

# Fájlnak a bezárása .close() metódussal
# Ennek különösen akkor van nagy jelentősége hogyha a fájlt nem csak olvassuk hanem irjuk is
# Hiszen hogyha nem zárjuk be a fájlt a fájlműveleteknek a végén akkor ebben az esetben adatveszteségis felléphet.

forrasfajl.close()

# Ennél van egyszerübb mód is a pythonban: with:Context manager
# with kulcsszó utána open() függvény a megfelelő paraméterekkel
# Ebben az eseben a fájl objektum nevének a megadását az as kulcsszó után tudjuk megtenni(ebben az esetben a forrasfajl)
# Majd egy kettőspont, és minden fájlhoz kapcsolodó múveletet majd itt ezen a blokkon belül fogjuk tudni megoldani
# Itt fogjuk ezt megvalósitani
# Ebben az esetben tehát nem kell aggódnunk a fájlnak a bezárásáról mivel helyettünk is megteszi a Context manager
# Ez a lehető legpraktikusabb megoldás akár a fájl olvasására akár az irására.

with open('adatok/szamozott_sorok.txt') as forrasfajl:
    print(forrasfajl.name, forrasfajl.mode)

# forrasfajl.name a fájlnak a nevét adja vissza
# forrasfajl.mode a fájlnak a módja (ebben az esetben ez az alapértelmezett, a read)
# Ezt meg is adhattuk volna határozott, explicit formában is:

# with open('adatok/szamozott_sorok.txt, 'r') as forrasfajl:

# Ebben az esetben is ugyan úgy futna le a fájlunk
# Ha egy v betűt vagy a betűt irnék akkor ebben az esetben már nem olvasnánk hanem létrehoznánk vagy hozzáfűznénk.


# Fájl beolvasás, tartalmának kiolvasása.
# .readline() metódus alapból az első sort fogja beolvasni
with open('adatok/szamozott_sorok.txt') as forrasfajl:
    print(forrasfajl.readline())

# Vigyázni kell az ékezetes betűkkel(Windows-on) mivel alapból nem megfelelően fogja kiiratni
# A megfelelő megjelenités érdekében megkell adni hogy utf-8 karakerkódolással történjen
# ehhez pedig meg kell adni az úgynevezett encoding paramétert, és utána pedig string formájában adhatjuk meg
# A kódolásnak a tipusát, és akkor az ékezetes beűk is probléma nélkül megjelennek.


with open('adatok/szamozott_sorok.txt', 'r', encoding='utf-8') as forrasfajl:
    print(forrasfajl.readline())
    print(forrasfajl.readline())  # Ha megint megadjuk a beolvasást akkor már a 2. sort fogja
    # A sorok végén habár nem látszik de a txt fájlban elhelyezkedik egy \n avagy új sor vezérlő karakter

# Létezik egy úgynevezett fájlmutató amely a fájl beolvasásával együtt halad
# Avagy először az első sorra mutat mikor beolvassuk, de mikor már másodszorra tesszük ezt meg
# Akkor már a 2. sorra fog mutatni

# A fájlmutatónak az aktuális értékét bájtban kifejezett értékét le is lehet kérni
# A .tell() metódus segitségével

with open('adatok/szamozott_sorok.txt', 'r', encoding='utf-8') as forrasfajl:
    print(forrasfajl.tell())
    print(forrasfajl.readline())
    print(forrasfajl.tell())
    print(forrasfajl.readline())
    print(forrasfajl.tell())

# Arra is módunk van hogy ne csak lekárjük ezt az információt hanem módositjuk is.
# Pl.: Tehát tegyük meg azt hogy az első sor beolvasása után a fájlmutatót vissza küldjük a fájlnak az elejére.
# Ezt a .seek() metódus segitségével tudjuk megtenni és a zárójel között meg kell adni a bájtban kifejezett értéket
# Ha a fájlnak az elejére szeretnénk akkor 0-t adunk meg

with open('adatok/szamozott_sorok.txt', 'r', encoding='utf-8') as forrasfajl:
    print('-----------------')
    print(forrasfajl.tell())
    print(forrasfajl.readline())
    forrasfajl.seek(0)
    print(forrasfajl.tell())
    print(forrasfajl.readline())
    print(forrasfajl.tell())

# A .seek() egyébként két paramétert is használ
# Az egyik az eltolásnak a mértéke
# A másik pedig a honnan avagy honnan valósul meg ez az eltolás
# Ez lehet: 0 (ez vissza küldi a fájlnak az elejére), 1 (az éppen aktuális pozició), 2(fájlnak a végét)
# forrasfajl.seek(0, 0), forras.seek(0, 1), forras.seek(0, 2)
# Az eltolás bájtban történik, ennek főleg a bináris fájlok beolvasásánál van jelentősége-
# Mig a legtöbbször a szöveges fájlok esetében a fájlmutatót az elejére szoktuk vissza küldeni
# Hogyha többször is szeretnénk beolvasni a fájlt anélkül hogy megkéne újra nyitni,
# Tehát akkor ebben az esetben ebben a formában tudjuk megtenni.

# Az open() függvény segitségével nem csak szöveges fájlokat tudunk megnyitni.
# Hanem bármilyen más fájlt is tudunk kezelni ebben az esetben viszont a módot ki kell egésziteni egy b betűvel(igy 'rb' lesz).
# És ez utal arra hogy bináris fájlokkal szeretnénk dolgozni

# with open('adatok/szamozott_sorok.txt', 'rb', encoding='utf-8') as forrasfajl:


# A .readline() melett létezik az úgynevezett .readlines() és ennek hatására az összes sor beolvasásra kerül
# És ezek a sorok egy listában rendezetten érhetőek el.
# Egy egy sor egy egy listaelem string formában, és itt már látszanak azok a \n sorvégi vezérlő karakterek

with open('adatok/szamozott_sorok.txt', 'r', encoding='utf-8') as forrasfajl:
    print(forrasfajl.readlines())

# A tömeges beolvasásnak van egy másik módja is.
# a .read() metódussal
with open('adatok/szamozott_sorok.txt', 'r', encoding='utf-8') as forrasfajl:
    print(forrasfajl.read())

# A .readlines() és a .read() hátránya az hogy ha nagyméretű a fájlunk akkor akár memória túlcsordulást is eredményezhet
# Ezért átalában inkább a soronkánti beolvasást szoktuk preferálni.

# A legegyszerübb:
# A forrasfajl nevű fájlobjektumunk bejárása egy for ciklussal
# A .strip() metódus eltávolitja a soremelési karaktereket.

print('---------------')
with open('adatok/szamozott_sorok.txt', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        print(sor.strip())


# CSV fájlok

# A CSV fájlok esetében a határoló, az adatokat elválasztó karakter egy soron belül az a vessző vagy a pontos vessző.
# Beolvasása.
print('-------------')
with open('adatok/autok_listaja.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        print(type(sor)) # Ezek stringek
        print(sor.strip())
        # Stringek feldarabolása a vesszők mentén a .split() metódussal
        print(sor.strip().split())
# Hogyha a .split() metódusnál nem adunk meg semmilyen argumentumot akkor a wildspace karakterek mentén
# pl.: tabulátorok, vagy a szóközök mentén kerül feldarabolásra a string
# Viszont mi itt meghatározhatunk egy kifejezett karaktert is, és ebben az esetben ez a vessző lesz amelyet string formájában
# aposztrofok között kell megadnunk

print('-------------')
with open('adatok/autok_listaja.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        print(sor.strip().split(','))

# És ennek hatására már egy lista fog keletkezni a listának az elemei pedig vesszővel elválaszott adatok
# És ezek ugyebár igy egy háromelemű listát eredményeznek amelyben minden egy egyes elem string tipusu és ez igaz minden egyes sorra

# Fájl tartalma rögzitése egy egységes adatszerkezetben

print('-------------')
autok = []

with open('adatok/autok_listaja.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        auto = {
                'rendszam': adatok[0],
                'tipus':    adatok[1],
                'kor':      int(adatok[2]),
                }
        autok.append(auto)

print(f'{autok=}')

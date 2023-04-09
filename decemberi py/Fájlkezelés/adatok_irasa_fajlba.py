# Megnyitási módok:
# r: olvasás
# w: írás, fájlt hoz létre; ha léztezik ilyen nevű fájl már, felülírja az eredetit
# x: írás, fájlt hoz létre; ha léztezik ilyen nevű fájl már, hibát ad
# a: a létező fájl végére hozzáfűz, ha még nem létezik ilyen nevű, akkor létrehozza
# a+: hozzáfűzést és olvasást is lehetővé tesz


# Érdemes egy eltérő változónevet használni a readdel szemben.
# Paraméterek között már az új fájlnak a nevét kell megadni
# Illetve egy másik módot amely az irásra szolgál.

# A printnél megszokott hogy a megadott érték az az elsődleges kimenetre, a képernyőre kerül.
# Ezt a célt viszont áttudjuk irányitani egy fájlra.
# file= paraméterrel. Itt megkell adni annak a fájl objektumnak a hivatkozását, referenciáját,
# Ahova szeretnénk ezt az értéket elmenteni.
# Ha már létezik ilyen fájl akkor az felülirásra kerül a w opció hatására.

with open('adatok/kimenet.txt', 'w', encoding='utf-8') as celfajl:
    print('Ez kerül mentésre.', file=celfajl)

# Meglévő fájlhoz való hozzáfűzés, bővités
# Ebben az esetben az a módot kell használni (append)
# Az a csak egy irása képességet, hozzáfűzési képességet pontosan
# Ami a fájlnak a végére fűzi hozzá az általunk kiirni szándékozott értékeket.
# Egyébként hogyha nem létezik ez a fájl akkor létre is hozza az a mód révén, viszont olvasni a fájlból nem tudunk.


with open('adatok/szamozott_sorok.txt', 'a', encoding='utf-8') as celfajl:
    print('Ez kerül mentésre!!!!!', file=celfajl)
    # celfajl.seek(0)
    # print(celfajl.readline()) #Hibát eredményez (not readable) mivel ezzel a móddal nem vagyunk képesek az olvasásra


# Megoldás: a+

with open('adatok/szamozott_sorok.txt', 'a+', encoding='utf-8') as celfajl:
    print('Ez kerül mentésre!!!!!', file=celfajl)
    celfajl.seek(0)
    print(celfajl.readline())

# A fájlmutató gyakorlatilag az olvasáshoz kötött, igy alapesetben és nem befolyáolja azt hogy ha az a módot adjuk meg.
# Akkor mindig a fájlnak a legvégére fogjuk irni a mentésre szánt értéket

with open('adatok/szamozott_sorok.txt', 'a+', encoding='utf-8') as celfajl:
    celfajl.seek(0)
    print(celfajl.readline())
    print(celfajl.tell())
    print('Ez kerül mentésre!!!!!', file=celfajl)

# Vajon a program melyik pontján megy végbe az irás?:

# Csak az input megadását követően kerül mentésre a kivánt érték.
# A fájlműveleteknél ugyanis létezik egy úgynevezett puffer amibe kerül a kiirásra szánt érték és ez a programnak csak
# Egy bizonyos pontján kerül üritésre. Ez egyébként függ a puffernek a méretétől is, hogy mennyi érték van benne.
# És ez gyakorlatilag tőlünk függetlenül szabályozott.
# Illetve ennek a puffernek az üritését mi magunk is kezdeményezhetjük:
# A flush = paraméterrel, ez alapből False
# Ha True-ra állitjuk akkor ebben az esetben azon a ponton kerül kiirásra az érték.
# Mivel már megtörtént a kiirás ezért amikor megadunk egy értéket akkor már csak a fájlnak a lezárása marad.
# A fájl tartalom már ilyen módon nem mődosul

with open('adatok/szamozott_sorok.txt', 'a+', encoding='utf-8') as celfajl:
    print('Ez kerül mentésre!!!!!', file=celfajl, flush=True)
    input('>')

# Fájl irásának további módjai.

# Fájl irásakor amikor printet használunk akkor alapesetben ahogy a print is alapesetben működik mindig új sorba ir
# A fájl esetén is persze ezt az end='' paraméter használatával felülirhatjuk.
# De egyébként használhatjuk ezt a .write() metódust is, és akkor ennek hatására erről nem is kell gondoskodnunk.
# Hogyha egymás mellé szeretnénkk elhelyezni stringeket, szövegrészleteket vagy akár egy-egy karaktert
# Akkor ebben a formában is megtudjuk ezt valósitani.

# A .writelines() metódusnál egy listát vagy bármilyen bejárható objektumot kell megadni.
# Itt arra kell ügyelni hogy a lista elemei kerülnek majd irásra, de ezek egymás mellé kerülnek, tehát itt sem lesz határoló karakter.
# pl.: Hogyha új sorba szeretnénk őket kiirni akkor erról nekünk gondoskodni \n megadásával
# Hogyha a .write() vagy .writelines() metódust hasznájuk akkor is van persze módunk arra hogy üritsük a puffert
# A .flush() metódussal
with open('adatok/szamozott_sorok.txt', 'a+', encoding='utf-8') as celfajl:
    # print('Ez kerül mentésre!!!!!', file=celfajl)
    celfajl.write('a')
    celfajl.write('b')
    celfajl.writelines(['alma', 'körte'])
    print('\n--------------', file=celfajl)
    celfajl.writelines(['alma\n', 'körte\n'])
    celfajl.flush()

# Szöveges fájl tartalmának másolása

# Egymás után két fájlt nyitok meg. Egyiket olvasásra a másikat pedig irásra

with open('adatok/szamozott_sorok.txt', 'r', encoding='utf-8') as forrasfajl:
    with open('adatok/szamozott_sorok_masolat.txt', 'w', encoding='utf-8') as celfajl:
        for sor in forrasfajl:
            print(sor.strip(), file=celfajl)

# Lehet egy sorban is:

with open('adatok/szamozott_sorok.txt', 'r', encoding='utf-8') as forrasfajl, open('adatok/szamozott_sorok_masolat.txt', 'w', encoding='utf-8') as celfajl:
        for sor in forrasfajl:
            print(sor.strip(), file=celfajl)

# Illtve lehet sortörést is használni hogyha nagyon hosszú a sor.
# A perjel jelzi  hogy ez igazából egy sorban helyezkedik el a forráskódunkban

with open('adatok/szamozott_sorok.txt', 'r', encoding='utf-8') as forrasfajl, \
        open('adatok/szamozott_sorok_masolat.txt', 'w', encoding='utf-8') as celfajl:
        for sor in forrasfajl:
            print(sor.strip(), file=celfajl)


# Létező fájlt autómatikusan felülirája akaratunk ellenére
# Megoldás: x mód (Hibaüzenetet eredményez amelyet a kivételkezeléssel elkerülhetjük)

# JSON = JavaScript Object Notation röviditése
# A JSON nyelvfüggetlen emiatt rengeteg webes aplikáció használja ezt a szerver és a kliens közötti adatcseréhez
# A JSON is a szótárhoz hasonlóan kulcspárokkal dolgozik amelyeket most név és értékpárnak neveznek
# Párok képezik a JSON formátumnak az alapját
# Az egész fájl egy kapcsos zárójelben helyezkedik el (elején megnyitjuk, végén bezárjuk)

# A név az mindig string és kizárólag idézójelek között szerepelhet, itt nem lehet aposztrofot használni
# Az értéket többféle adattipus valósithatja meg,
# Egy részről természetesen lehet ez is string, lehet true vagy false érték (kis kezdőbetűvel irva)
# Lehet null hogy ha nem adunk meg értéket
# Illetve természetesen szerepelhetnek számok, egész számok vagy decimális számok ennek itt nincs külön tipusa, de mind a kettőt használhatjuk
# Azon kivül használhatunk itt is a JSON formátumon belül is gyűjteményeket, tömböket.
# A név értékpárokat egymástől vesszővel választjuk el.
# A behúzásoknak, a wildspace karaktereknek feldolgozás szempontjából igazából nincs jelentősége
# Ezeket azért tesszük meg hogy könnyebben olvasható legyen az emberi szem számára, könnyen értelmezhetők legyenek ezek az adatok


# JSON fájl beolvasása, adatok értelmezése

# be kell importálni a json modult
# Vigyázni kell hogy a pyton fájlt ne csak simán json.py-nak nevezzük el hanem ezt valamilyen módon bővitsük
# Mivel az import úgy müködik hogy először a saját könyvtárban kutakodik, és akkor a saját fájlt próbálta volna beimportálni.
# Context managerrel meg kell nyitni a fájlt
# json modulnak a load függvényét kell használni a beolvasáshoz, itt paraméterként meg kell adni a fájlunknak a referenciáját
# Ezt egy változóban tárolandó hogy hivatkozni is lehessen rá.
# Egy szótár lesz belőle
# Van egy szabályos kulcs amihez pedig egy python lista tartozik amelynek elemei szótárak ezek pedig az értékek
# A jSON adattipusok konvertálásra kerültek
# pl.: true értékből True lett , false értékből False lett, null értékből None lett,
# Ezért is fontos használni a json modulnak a load függvényét hogy ezek az értékek illetve tárolók konvertálásra kerüljenek a szabályos python formátumunká


import json

with open('./adatok/diakok.json', 'r', encoding='utf-8') as diak_adatok:
    adatok = json.load(diak_adatok)
    print(type(adatok))
    print(adatok)

# Adatok megjelenitése for ciklussal
# Arra is módunk van hogy ebbe a szabályos szótár szerkezetbe mi belepiszkáljunk módositjunk

with open('./adatok/diakok.json', 'r', encoding='utf-8') as diak_adatok:
    adatok = json.load(diak_adatok)
    for diak in adatok['diakok']:
        diak['osztály'] = '10C'
        print(diak)

# JSON fájl létrehozása
# Igy az adatcserének mindkét végén gyakorlatilag jelen tud lenni a python programunk nem csak fogadni tud hanem késziteni is JSON fájlokat.
# Ezt a json.dump() függvénnyel lehet.
# Itt meg kell adni egy objektumot jelen esetben a python szótárunkat, utána át kell adnunk a fájlnak a referenciáját.

# Ez tartalmazni fogja az adatokat, de két dolog fel is tünik:
# A karakterkódolás : ékezetes betük esetébem vezárlőkarakterek jelennek meg
# A whitespace karakterek nem kerültek be és emiatt nehezen olvasható a fájlunk
# Igy nézne ki a json fájlban:
# {"diakok": [{"n\u00e9v": "Kis P\u00e9ter", "email": ["kiss@suli.hu", "petike@otthoni.hu"], "kollegista": true, "oszt\u00e1ly": "10C"}, {"n\u00e9v": "Nagy Zo\u00e9", "email": null, "kollegista": false, "oszt\u00e1ly": "10C"}]}
# A whitespace karakterek berakását az indent= paraméterrel lehet megvalósitani, ahol meg kell adni a behúzásnak a mértékét, ez lehet 2 vagy akár 4 is

with open('./adatok/diakok_masolat.json', 'w', encoding='utf-8') as diak_adatok2:
    json.dump(adatok, diak_adatok2, indent=2)

print('----------------------')
# A vézérlőkarakterek egyáltalán nem jelentenek problémát a fájl beolvasásakor

with open('./adatok/diakok_masolat.json', 'r', encoding='utf-8') as bemenet:
    adatok_2 = json.load(bemenet)
    for diak in adatok_2['diakok']:
        print(diak)
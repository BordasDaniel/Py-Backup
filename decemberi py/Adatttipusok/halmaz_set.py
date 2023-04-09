# Halmazok tulajdonságai.
"""
- Egyszerre csak egy elem(listák esetében megengedett volt az ismétlődés a halmazok esetében viszont kizárt)
- Rendezetlen
- Többféle tipust is tárolhat egyszerre (mint a listák, avagy egy tároló egyszerre több tipust tartalmazzon)
- Az elemeket nem lehet megváltoztatni(a listák esetében mint mikor stringeket tartalmazott lehetőségünk volt arra,
hogy a stringekhez hozzáférjünk és átalakitsuk őket)
- unió, metszet, különbség (Akár a matekban)
"""

# Halmazok létrehozása.
# Használata: Gyűjtemény neve = {elemek neve kapcsos zárójel között, vesszővel elválasztva}

reggeli = {'vaj', 'tea', 'piritos'}

# Üres halmaz

ebed = {}  # Igy egy szótár lesz
print(type(ebed))

ebed = set()  # Igy már halmaz
print(type(ebed))

# Különbség a szótár és a halmaz között.
"""
Ránézésre meglehet őket különiteni, hiszen a szótárak esetében mindig kulcs és értékpárokról beszélünk.
Mig a halmazok esetében önállóan egyesével kerülnek felsorolásra.
"""
# Ha a konstruktort meghivjuk (set()) és egy listát adunk meg akkor igy is keletkezhet egy halmaz.
ebed = set(['halászlé', 'kenyér', True, True])
# Mivel az ismétlődés nem megengedett emiatt az hogy két true érték van a halmazban a tartalmát nem fogja befolyásolni
# Hiszen egy elemet csak egyszer tartalmazhat.
print(type(ebed))
print(ebed)  # Mivel rendezetlen emiatt nem pontosan ugyan azt a sorrendet kapod vissza.


# Halmaz bővitése
# .add('argumentum') metódussal
# Szintén ha egy olyan elemet akarok hozzáadni amely már benne van a halmazban akkor semmi nem fog változni.

reggeli.add('viz')
print(reggeli)

# Halmaz elemet eltávolitása.
# .remove('argumentum') metódussal
# Ha egy olyan elemet távolitunk el amely benne sincs a halmazban akkor KeyErrort fogunk kapni.

reggeli.remove('tea')
print(reggeli)

# KeyError elkerülhető a .discard('argumentum') metódussal
# Ha benne van az elem a halmazban akkor eltávolitja ha nincs akkor nem csinál semmit.

reggeli.discard('körte')
print(reggeli)

# Halmazműveletek:

# Metszet.
# Egy halmazzal tér vissza amelyben csak azok az értékek szerepelnek amelyek mind a kettőben benne vannak.
# Ha nincs olyan elem akkor egy üres halmazzal tér vissza.

reggeli = {'viz', 'tea', 'piritós'}
ebed = {'viz', 'halászlé', 'kenyér'}
print(reggeli & ebed)

# Unió.
# A két halmaz összes elemét egy halmazba teszi és azzal tér vissza.
# Szintén nincs duplikáció elemek esetében avagy nem lehet kettő 'viz' elem.

print(reggeli | ebed)

# Két halmaz különbsége.
# Az elsőnek megadott halmazból kivonja a másodiknak megadott halmaz elemeit és igy tovább.
print(ebed - reggeli)
print(reggeli - ebed)

# Ebben az esetben pedig csakis olyan elemeket kapunk amelyek vagy csak az egyik halmaznak
# Vagy csak a másik halmaznak voltak a részei.
print(reggeli ^ ebed)


# Halmazok leggyakoribb felhasználhatósági esete:
# Egy listában ismétlődő elemek vannak és mi ezeket el szeretnénk távolitani.

gyumolcskosar = ['eper', 'alma', 'szilva', 'eper']
fajta = set()
for gyumolcs in gyumolcskosar:
    fajta.add(gyumolcs)
print(fajta)
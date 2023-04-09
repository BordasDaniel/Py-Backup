# Üres szótár létrehozása

raktar = {}
print(raktar)

# Szótár létrehozása adatokkal

diak = {
    'vezeteknev': 'Kiss',
    'keresztnev': 'Péter',
    'eletkor': 17,
    'menza': True,

}
print(diak)
print(diak['eletkor'])  # Kulcs megadásával érjük el az értéket.
print(diak.get('eletkor'))  # .get() metódussal

try:
    print(diak['szakkor'])  # Nem létező kulcsra való hivatkozás során hibát kapunk.
except:
    print('Hiba')

# Key error elkerülése .get() metódussal
# Ha nem találja az adott kulcsot akkor egy adott értékkel térjen vissza amelyet én határozhatok meg.

print(diak.get('szakkor', 'nincs adat'))

# A kulcsra való hivatkozás elött leellenőrizni hogy létezik-e a kulcs.
# True vagy False értékkel tér vissza.

print('szakkor' in diak)

# Új kulcspár létrehozása.

diak['szakkor'] = True
print(diak)

# Érték felülirása.

diak['eletkor'] = 20
print(diak)

# Adott kulcs törlése. Ezzel együtt az értéke is törlésre kerül.

del diak['vezeteknev']
print(diak)


# Kulcs hozzáférése for ciklussal.

diak = {
    'vezeteknev': 'Kiss',
    'keresztnev': 'Péter',
    'eletkor': 17,
    'menza': True,
    'matek_jegyek': [5, 4, 4, 3, 5, 5]
}

for kulcs in diak:
    print(kulcs, diak[kulcs])

# A .values() metódus segitségével azonnal a szótar értékeihez férünk hozzá amelyek egy listában vannak.

print(diak.values())

# Értékek egymás alá irása for ciklussal.

for ertek in diak.values():
    print(ertek)

print(diak.items())  # Tuples-t kapunk vissza.
for kulcs, ertek in diak.items():
    print(kulcs, ertek)

# Egymásba ágyazott szótérak.
"""
Láttuk, hogy a szótárban az érték gyakorlatilag bármilyen akár összetett adattípus lehet, pl. lista.
Egy szótár ennek megfelelően tartalmazhat további szótárakat is. 
Az alábbi példán a kulcs (key) a 'cim', az ehhez tartozó érték (value) pedig egy szótár:
"""

diak = {
    'vezeteknev': 'Kiss',
    'keresztnev': 'Péter',
    'osztaly': '10.A',
    'eletkor': 17,
    'cim': {
        'iranyitoszam': 9400,
        'varos': 'Sopron',
        'kozterulet': 'Fő utca',
        'hazszam': 5
    }
}

"""
A szótárak egymásba ágyazása elméletileg korlátlan mélységig megvalósulhat. 
Az egymásba ágyazásnak igazából csak az átláthatóság szab határt.
Hogyan férhetünk hozzá egy beágyazott szótárban tárolt értékhez?
"""

print(diak['cim']['iranyitoszam'])

sebessegek = ['12.3', '31.7', '28.4', '9.0']

#Lista elemeit int tipussá alakitani:


# for ciklussal
atalakitott = []

for sebesseg in sebessegek:
    tizedes_tort = float(sebesseg)
    atalakitott.append(tizedes_tort)


print(atalakitott)
print(f'{atalakitott=}') 
# Az egyenlő nem csak a gyűjtemény elemeit hanem a nevét is megfogja jeleniteni.

#listaértelmezéssel

int_sebessegek = [float(x) for x in sebessegek]
print(f'{int_sebessegek=}')


# map() függvénnyel

# map(fgv, tarolo)
# Működése: Fogja a bejárható objektumot és minden egyes elemén meghivja majd azt a függvényt amit 1. argumentumként megadtunk.
# alap esetben egy map objektummal tér vissza, ezért egy listába kell tenni.
# nem csak beépitett függvényeket hanem akár saját magunk által beépitett függvényeket is használhatunk


atalakitott = list(map(float, sebessegek))
print(atalakitott)



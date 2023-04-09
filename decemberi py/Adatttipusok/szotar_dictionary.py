
diak = ['Kiss', 'Peter', '10.A', 17, True, False]
print(diak[3])


# A szótárban egyes értékekhez cimkét, megnevezést vagy bármilyen tipust rendelhetünk hozzá.
# Olyat ami számunkra praktikus, ebben az esetben stringek formájában rögzitjük ezeket a megnevezéseket.


diak = {
    'vezeteknev': 'Kiss',
    'keresztnev': 'Péter',
    'osztaly': '10.A',
    'eletkor': 17,
    'kollegista': True,
    'info_fakt': False,
}
print(diak['eletkor'])

# A szótárban mindig adatpárokat tárolunk.
# Az adatpár egyik tagja a kulcs (key) pl.:'eletkor' a másik pedig az érték (value) pl.: 17
# Egy értékhez mindig egy adott kulcs révén férünk hozzá. Mind a 2 lehet különböző tipus(lehet összetett is pl.: lista).
# Ebben a példában az összes kulcs string tipusu az értékek viszont különbözőek.

# Raktár példája, ahol az árucikkeket különböző sorozatszámmal különitjük el egymástól.
# Itt a kulcs az int tipusu.

raktar = {
    114589: 'Dominó polc',
    264875: 'Student íróasztal',
    364879: 'Kényelem01 fotel',
    568974: 'Family étkezőasztal 6 fős',
}

# Ha sok adat van akkor inkább szótárt használjuk kétdimenziós lista helyett.
# Olvashatóság szempontjából is jobb mivel nem index hanem elnevezés alapján hivatkozuk a szótár elemére.

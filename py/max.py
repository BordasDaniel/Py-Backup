nevek = []
nev = None

while len(nevek) != 3 and nev != '':
    nev = input('Add meg a neved!: \t')
    nevek.append(nev)
    if len(nevek) == 3:
        print('Sajnos negyedik név megadására nincs lehetőséged!')
print((' ').join(nevek))
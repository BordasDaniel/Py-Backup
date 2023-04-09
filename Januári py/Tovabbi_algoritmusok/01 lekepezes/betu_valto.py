# Metódus példák:

# lower(), upper(), capitalize(), swapcase()
# Eldontő metódusok:
# islower(), isupper(), isalpha(), isdecimal()


eredmeny = 'ALMA'.lower()
print(eredmeny)

eredmeny = 'alma'.upper()
print(eredmeny)

eredmeny = 'alma'.capitalize()
print(eredmeny)

eredmeny = 'alma'.swapcase()
print(eredmeny)

eredmeny = 'Alma'.isupper()
print(eredmeny)

eredmeny = 'ALMA'.isupper()
print(eredmeny)


def atvalto(szo):
    return szo.lower()

gyomolcsok = ['ALMA', 'KÖRTE', 'EPER', 'BANÁN']

# map() függvénnyel

# metódus neveket nem lehet megadni csak függvényeket

atalakitott = list(map(atvalto, gyomolcsok))
print(atalakitott)
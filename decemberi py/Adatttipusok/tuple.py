# A tuple tulajdonságai:
"""
-rendezett (Az elemeknek indexe van)
-egy elem többször is lehet benne
-több tipust is tárolhat, akár egyszerre is
-nem megváltoztatható(immutábilis):
    -elemeket
    -elemek sorrendjét
    -elemek számát
"""

# Tuple létrehozása
# A listához hasonlóan itt is az elemeket vesszővel elválasztva soroljuk fel.

pelda_tuple = (0, 5)
print(pelda_tuple, end='\t')
print(type(pelda_tuple))

# Zárójeltől függetlenül jöhet létre tuple
pelda_tuple2 = 2, 4
print(pelda_tuple2, end='\t')
print(type(pelda_tuple2))

# Tuple kicsomagolása.

x, y = pelda_tuple
print('x =', x, type(x))
print('y =', y, type(y))

# Tuple tulajdonságai példákkal.

# Több tipust is tárolhat, akár egyszerre is
pelda_tuple3 = (1, 3.2, True, 'alma')
print(pelda_tuple3, end='\t')
print(type(pelda_tuple3))

# Rendezett (Az elemeknek indexe van)
print(pelda_tuple3[2])

# Nem megváltoztatható(immutábilis).
try:
    pelda_tuple3[2] = False
except:
    print('Type Error lenne')

# Tuple gyakorlati alkalmazása:
# Pl egy koordináta pontnak a meghatározására, szinek(RGB)

KEK = (0, 0, 255)
FHD = (1920, 1080)
HD = (1280, 720)

lista = ['Debrecen','Sopron','Pécs']

for index, elem in enumerate(lista):
    print(index, elem)

for index, elem in enumerate(lista):
    print(index, end='\t')
    print(type(index))

# Az enumerate visszatérési értéke egy tuple
for x in enumerate(lista):
    print(x, end='\t')
    print(type(x))

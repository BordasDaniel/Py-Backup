# 1. feladat.
"""
this_tuple = False, True
try:
    this_tuple[0] = True
except:
    print('Ez egy error lett')
"""
# 2. feladat

import ast

RGB = ast.literal_eval(input('Ird be a szinkombinációd!\t'))
print(RGB)

szinek = {
    'Vörös': RGB[0],
    'Zöld':  RGB[1],
    'Kék':   RGB[2],
}

if RGB[1] > 0:
    print('Tartalmaz zöldet!')

min = 0
for x in RGB:
    if x > min:
        min = x


index = RGB.index(min)

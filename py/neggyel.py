''' 
import random
szamok = []
szam = None
osszes = []

while len(osszes) != 10:
    szam = random.randint(0,50)
    osszes.append(szam)
    if szam %4 == 0:
        szamok.append(szam)
print("A néggyel osztható számaid : ",szamok)
print("Ezeknek a mennyisége: ",(len(szamok)))
print("Az összes szám: ",(osszes))
'''


import random

szam = None
szamok = []
osszes = []

for i in range(0,10):
   szam = random.randint(0,50)
   osszes.append(szam)
   if szam %4 == 0:
    szamok.append(szam)

print(szamok)
print(len(szamok))
print(osszes)
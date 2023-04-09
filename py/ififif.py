import random
import math

szam = random.randint(-5 , 5)
print(szam)


#Nem jó
'''
if szam > 0:
     print("A szám pozitiv")
elif szam < 0:
     print("A szám negativ")
else:
     print("A szám semleges")
'''

#Jó
'''
if szam > 0:
     print("A szám pozitiv")
if szam < 0:
     print("A szám negativ")
if szam == 0 :
     print("A szám semleges")
     '''


if szam > 0:
    print("Pozitiv")
if szam % 2 == 0:
    print("Páros")
if szam == 2 or szam == 3 or szam == 5:
    print("Prim")


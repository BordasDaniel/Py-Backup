import math
import random 

gondolt = random.randint(0, 100)
tipp = int(input("Szerintem a te számod a : "))

while gondolt != tipp:
    print("Sajnos tévedtél. Tippelj újra adok egy kis segitséget!")   
    if gondolt < tipp:
        print("Kisebb")
    else: #if gondolt > tipp: (EZ VOLT EREDETILEG)
        print("Nagyobb")
    tipp = int(input("Szerintem a te számod a : "))

if gondolt == tipp: 
    print("Gratulálok eltaláltad!")








'''
import math
import random 

gondolt = random.randint(0, 100)
tipp = int(input("Szerintem a te számod a : "))

while gondolt != tipp:
    print("Sajnos tévedtél. Tippelj újra adok egy kis segitséget!")   
    if gondolt < tipp:
        print("Kisebb")
    if gondolt > tipp:
        print("Nagyobb")
    tipp = int(input("Szerintem a te számod a : "))

if gondolt == tipp: 
    print("Gratulálok eltaláltad!")


'''
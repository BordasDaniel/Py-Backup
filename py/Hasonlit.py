import random
import math

gep = random.randint(1,3)
sajat = int(input("Válassz egy számot 1 és 3 között! "))
print("Az én számom a:", gep, "A tiéd a:", sajat)
if sajat == gep:
    print("Nézd megegyeznek!")
else:
    print("Mindketten más számra gondoltunk!")
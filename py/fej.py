import math
import random



kapott = random.randint(1,2)
valasz = str(input("Fej vagy irás? "))

if valasz == "Fej" or "fej":
    valasz = 1
if valasz == "Iras" or "iras":
    valasz= 2


if kapott == 1:
     print("Fej")
if kapott == 2:
     print("Irás")

print(type(kapott))
print(type(valasz))

if kapott == valasz:
     print("Gratulálok eltaláltad")
else:
    print("Hát sajnos ez most nem jött össze! :(")


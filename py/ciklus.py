'''
szam = 1
while szam <= 10:
     print(szam)
     szam = szam + 1
'''

'''
szamlalo = 1
while szamlalo <= 5:
    print("Ok")
    szamlalo += 1
'''

folytatja = True
while folytatja:
    print("Vidd ki a szemetet!")
    valasz = input("Mondjam még egszer? (i/n) ")
    if valasz == "n":
        folytatja = False
print("A progmram vége.")
    
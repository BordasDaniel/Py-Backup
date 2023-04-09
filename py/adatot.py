'''
szam = int(input("Adj meg egy egész számot 5 és 10 között! "))

# while szam <5 or szam > 10:
while not 5 <= szam <= 10:
    szam = int(input("Helytelen érték! Adj meg egy egész számot 5 és 10 között! "))

print("Rendben!")
'''

szo = None
while szo != " ":
    szo = input("Adj meg szvakat! Ha kilépnél akkor egy szóközt nyomj! ")

print("Program vége!")
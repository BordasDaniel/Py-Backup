import math


# Szöveg összefonása
"""
 ker = str(input('Mi a keresztneved? : '))
 vez= str(input('Mi a vezetékneved? : '))
 teljes = vez + " " + ker
 print(teljes)
"""


print(2**-4)

# Alapok
'''
 print (4 + 2)
 print (4 - 2)
 print (4 * 2)
 print (4 / 2)
 print (9 % 2)
'''

# Százalék számitás
'''
print((9 / 100)*2)
'''

# Ha 0-tól eltérő számot kapunk akkor az maradék nélkül nem osztható azzal a számmal
'''
print(15 % 4)
print(16 % 4)
'''

print('alma' + 'fa' )

# Szó bekérése majd kiiratása
'''
megadott_szo = input("Adj meg egy szót! ")
print(megadott_szo)
'''

# Strből intbe
'''
bekert_adat = input("Adj meg egy számot! ")
szam = int(bekert_adat)
print(type(szam))
print(szam)
print(szam /2 )
'''

# Strből intbe(Azonnal)
'''
szam = int(input("Adj meg egy számot! "))
print(type(szam))
print(szam)
'''


#Több változó kiiratása egyszerre, print szabályozása.
'''
szam1 =  17
szam2 =  34
szam3 =  76
print(szam1, szam2, szam3)
print(szam1, szam2, szam3, sep=' # ', end='\t') #A \t jelentése egy tabulátornyi távolság(Lehet egyszerre több is egymás után)
print(szam1, szam2, szam3, sep=' # ')
print(szam1, szam2, szam3, sep=' # ', end='\t\t')
print(szam1, szam2, szam3, sep=' # ')
print(szam1, szam2, szam3, sep=' # ', end='\n') #A \n jelentése új sor(Lehet egyszerre több is egymás után)
print(szam1, szam2, szam3, sep=' # ', end='\n\n\n')
print(szam1, szam2, szam3, sep=' # ', end='   ')
print(szam1, szam2, szam3, sep=' # ')
'''

# Hatványozás
x = 5
x = x ** 3  # x = 125



# a = float(2)
# b= float(3)
# c= float(4)

# s = (a+b+c)/2
# print(s)
# terulet = math.sqrt(s*(s-a)*(s-b)*(s-c))
# print(terulet)

a = int(input("a oldala: "))
a = a**2
b = int(input("b oldala: "))
b = b**2
# c = int(input(c oldala: ))
# c = c*c
# c=?
c= math.sqrt(a+b)
print(c)

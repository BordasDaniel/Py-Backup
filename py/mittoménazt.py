szoveg = 'szia'
szam = 17
tizedes_tört = 3.14
oszthatoe = True
oszthatoe2 = False
print(tizedes_tört, szoveg, szam)


print(type(szoveg)) #str
print(type(szam)) #int
print(type(tizedes_tört)) #float
print(type(oszthatoe)) #bool
print(type(oszthatoe2)) #bool

test = 'alma'
print(test)
test = 17
print(test)

# szoveg → szam
szam = int('17')
print(type(szam))

# szoveg → tizedes_tort
szam = float('17.5')
print(type(szam))


# szam → szoveg
szam = str(17)
print(type(szam))
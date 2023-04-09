#Minden objektumnak más-más képességei vannak. pl.: list.sort(), int.__abs__(), str.islower(), float.__add__()

szam_1 = 350
szam_2 = 500
szamok = [3,2,1]
# szam_2 = szam_1

print(f'{szam_1=} | {type(szam_1)} | {id(szam_1)}')
print(f'{szam_2=} | {type(szam_2)} | {id(szam_2)}')
print(f'{szamok=} | {type(szamok)} | {id(szamok)}')


# Abszolút értékét határozza meg.
print(szam_1.__abs__())

#Szorirozza a listát növekvő sorrendre
szamok.sort()
print(szamok)

# Az a ugyanarra az objektumra mutat mint a b int esetében
a = 1234567
b = 1234567

print(id(a))
print(id(b))

# Lista esetében viszont két eltérő objektum jön létre.
c = [1,2,3]
d = [1,2,3]

print(id(c))
print(id(d))

# Az a ugyanarra az objektumra mutat mint a b str esetében
e = 'szo'
f = 'szo'

print(id(e))
print(id(f))

# Nem megváltoztatható objektumok (immutábilis/immutable):
'''
-int
-float
-bool
-str
-tuple
'''

# Megváltoztatható objektumok(mutáblis/mutable):
'''
-list
-dict
-set
'''


a = 300
b = 300

print(id(a))
print(id(b))

# Létrejön egy teljesen új objektum aminek eltér az azanositója.
# Nem az objektum tartalma változik meg.
a +=1
print(id(a))


c = [1,2,3]
d = [1,2,3]

print(id(c))
print(id(d))


# Az objektum tartalma változik de nem jön létre új.
c.append(17)
print(id(c))
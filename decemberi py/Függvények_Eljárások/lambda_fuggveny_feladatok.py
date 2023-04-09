# 1. feladat:
"""
lista = ['alma','barack','eper','meggy','körte']
print(sorted(lista, key=lambda masodik: masodik[1]))
"""
# 2. feladat:
'''
azonositok = ['id10', 'id100', 'id23', 'id2', 'id13', 'id1']    
print(sorted(azonositok, key=lambda id: int(id[2:])))
'''

# 3. feladat:
szavak = ['alma', 'ló', 'padló', 'citrom', 'kávé', 'nyugalom']    
print(list(filter(lambda szures: 'i' in szures, szavak)))
print([x for x in szavak if 'i' in x])

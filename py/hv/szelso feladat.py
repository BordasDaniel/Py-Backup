adat = []
beker = None
minmax = []

'''
while beker != 'x' and beker != 'X':
    beker = input('Adj meg egy számot!\t')
    if beker != "X" and beker != "x":
        adat.append(int(beker))
        if int(beker) %2 == 0:
            minmax.append(beker)

print(min(minmax))
print(max(minmax))
print(adat)
'''


while beker != '':
    beker = input('Adj meg egy szót\t')
    if not beker == '':
        adat.append(beker)

minim = adat[0]
maxim = adat[0]

#Hoszabb
'''
for x in adat:
    if len(maxim) < len(x):
        maxim = x
    if len(minim) > len(x):
        minim = x
'''

min = [x for x in adat if len(adat[0]) > len(x)]
max = [x for x in adat if len(adat[0]) < len(x)]

print(('').join(min))
print(('').join(max))
print(adat)
# print(maxim)
# print(minim)

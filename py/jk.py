import random
import time

b = random.randint(0,len('asd.txt'))
print(b)
lista = []
dupla = []
time.sleep(1)
i = str
c = 5

'''
while i in lista != i:
    for i in range(b):
        print(random.choice(list(open('asd.txt') )),end='')
        lista.append(i)
        time.sleep(0.75)
        if i in lista == i:
            dupla.append(i)
            break
        else:
            b += b



print(dupla)
'''
for i in open('asd.txt') in range(b):
    print(random.choice(list(open('asd.txt'))),end='')
    lista.append(i)
    time.sleep(0.75)


'''
print(lista)
print('Visszaszámlálás megkezdődött!')
time.sleep(1)
print(5)
time.sleep(0.75)
print(4)
time.sleep(0.75)
print(3)
time.sleep(0.75)
print(2)
time.sleep(0.75)
print(1)
time.sleep(0.75)
print(0)
time.sleep(0.75)
asd = random.choice(lista)
print( asd[0] ,'ez lett az eredmény')
'''


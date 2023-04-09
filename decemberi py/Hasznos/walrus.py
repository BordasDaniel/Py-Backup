
#Eredeti
'''import random

szam = random.randint(1,10)
print(f'{szam=}')

tipp = int(input('Tipp:\t'))
while tipp != szam:
    print('Sajnos nem!')
    tipp = int(input('\nTipp:\t'))

print('Kitaláltad!')'''

#------------------------------------------#

#Walrus operátorral:
#Az értékadás és a kiértékelés össze van vonva egy sorba


import random

szam = random.randint(1,10)
print(f'{szam=}')


while tipp := int(input('\nTipp:\t')) != szam:
    print('Sajnos nem!')
print('Kitaláltad!')

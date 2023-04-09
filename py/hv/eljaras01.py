def koszont():
    print('Üdv a fedélzeten!')
koszont()


def koszont_nevvel(nev):
    print('Szia '+ nev +', üdv a fedélzeten!')
koszont_nevvel('Ádám')

def koszont_ket_nevvel(nev1,nev2):
    print('Szia ' + nev1 + ' és ' + nev2 + ' üdv a fedélzeten')
    
koszont_ket_nevvel('Ádám','Éva')

def osszead(x,y):
    eredmény = x+y
    print('A két szám összege: ',eredmény)

osszead(1,2)
# osszead(1+3,40-2) #Lehet matematikai egyenlet is.
# a = 6 
# b = 7
#osszead(a,b) #Lehet változó is

def kiir():
    lokalis = 'alma'
    print(lokalis)
    print(globalis)

globalis = 'gyümölcs' #Az eljáráson kivüli változókra viszont lehet magában az eljárásban és azon kivül is hivatkozni. (Úgynevezett Globális változók)
kiir()
print(globalis)
#print(lokalis) #A változó az eljáráson kivül nem érhető el. (Úgynevezett Lokális változók)
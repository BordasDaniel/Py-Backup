def szamol(a,b,c):
    return (a+b)*c
print(szamol(1,2,3))


def szamol2(a,b,c=100):
    return (a+b)*c
print(szamol2(1,2)) 


def szamol3(a,b,c=1000):
    return (a+b)*c
print(szamol3(1,2,3000)) #Ha mégis megadom neki az argumentumot akkor az felülirja a már meglévőt.

def szamol4(a,b,c):
    return (a+b)*c
print(szamol4(c=10,a=2,b=4)) #A sorrend felcserélhető ha név szerint adjuk meg a paramétereket.


def max_kereso(x, *args):
    max = x
    for szam in args:
        if szam > max:
            max = szam
    return max

print(max_kereso(1,12,30,20,2000))

'''egy kötelező paraméter van, és a többi (tetszőlegesen sok)
paraméter az 'args' nevű listában tárolódik'''
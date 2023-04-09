"""
Írj egy programot, amely szótárban tárolja egy macska nevét, korát.
A felhasználónak legyen lehetősége megváltoztatni az egyik tárolt adatot.
A program írja ki a felhasználó választása alapján az egyik adatot, 
kérdezze meg, mire módosítsa, végül írja ki a képernyőre a frissített adatszerkezetet!
"""

def valtozas(macska, user):
    def kor_valtozas():
        macska['kor'] = int(input('Hány éves a macskád?\t'))
    def nev_valtozas():
        macska['nev'] = input('Mi a macskád neve?\t')
        

    if user == 'kor':
        kor_valtozas()
    else:
        nev_valtozas()



def valasztas():
    user = input('Mit szeretnél megváltoztatni?\nA nevét vagy a korát?\t')
    return user
        

def kiirat(macska):
    for x in macska:
        print(x, macska[x])


def adat():
    macska = {
        'nev': 'Boris',
        'kor': 4,
    }
    return macska

def main():
    macska = adat()
    kiirat(macska)
    user = valasztas()
    valtozas(macska, user)
    kiirat(macska)

main()
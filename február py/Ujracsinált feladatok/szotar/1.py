"""
Írj egy programot, amely a felhasználótól bekéri egy kutya nevét, életkorát, fajtáját,
és azt hogy rendelkezik-e érvényes oltással veszettség ellen! Az adatokat tárolja a program szótárban,
 és írja ki a képernyőre az adatszerkezetet!
"""

def adatok():
    kutya = {}
    kutya['nev'] = input('Mi a kutyád neve?\t')
    kutya['kor'] = int(input('Hány éves a kutyád?\t'))
    kutya['faj'] = input('Mi a kutyád faja?\t')
    kutya['oltas'] = input('Van oltása?\t')
    return kutya

def kiirat(kutya):
    for adat in kutya:
        print(adat, kutya[adat])


def main():
    kutya = adatok()
    kiirat(kutya)

main()
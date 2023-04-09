import random 


def szovalaszto():
    szotar = ['kalap', 'tégla', 'lámpa', 'tábla', 'kocsi']
    return random.choice(szotar)


def nem_megoldott(jatekos):
    return '_' in jatekos


def tipp_bekero():
    return input('Adj meg egy betűt!\t')


def ertekel(gep, karakter, jatekos, nem_jo):
    talalat = False
    for index, betu in enumerate(gep):
        if karakter == betu:
            jatekos[index] = karakter
            talalat = True
    if talalat:
        print('Találat!')
    else:
        print('Sajnos nem talált!')
        nem_jo.append(karakter)
    print(f'Jelenlegi állás : {"".join(jatekos)}')
    print(f'Roszz tippek {", ".join(nem_jo)}')
    print('-------------------------------------------\n')
    

def main():
    print('Találd ki, melyik 5 betűs főnévre gondoltam!')
    kitalalando = szovalaszto()
    allas = ['_', '_', '_', '_', '_']
    rossztippek = []
    probalkozasok = 0
    while nem_megoldott(allas):
        probalkozasok += 1
        tipp = tipp_bekero()
        ertekel(kitalalando, tipp, allas, rossztippek)
    print(f'Gratulálok! Kitaláltad {probalkozasok} próbálkozásból.')


main()

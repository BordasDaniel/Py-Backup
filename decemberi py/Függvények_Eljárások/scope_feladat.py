import random


def tipp_bekero():
    szam = int(input('Add meg a számot amire gondoltál!'))
    return szam


def main():
    print('Gondoltam egy számra 1 és 10 között! Próbáld meg kitalálni!')
    talalat = False
    while talalat != True:
        tipp = tipp_bekero()
        talalat = eltalalta(tipp,kitalalando)
    print(f'Gratulálok eltaláltad {proba} próbálkozásból')
    print('Játék vége!')




def eltalalta(tipp,kitalaldo):
    global proba
    proba = proba +1
    if tipp == kitalalando:
        return True
    else:
        print(f'Nem talált! Ez volt a {proba}. próbálkozásod! ')
        return False


kitalalando = random.randint(1,10)
proba = 0
print(kitalalando)
main()




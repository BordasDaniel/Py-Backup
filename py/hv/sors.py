import random
lett = None
szam = 0


def ker():
    megad = int(input('1 vagy 2 ?\t'))
    return megad

def robot():
    lett = random.randint(1,2)
    return lett


while szam != lett:
    szam = ker()
    lett = robot()
    print(lett)





    

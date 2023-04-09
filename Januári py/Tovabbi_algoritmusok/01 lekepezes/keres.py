def keres(felso, also):
    lista = []
    szam = 1
    for x in range(1, 100):
        if felso%szam == 0 and also%szam == 0:
            lista.append(x)
        szam += 1
    return lista

mehet = True
while mehet :
    felso = float(input('Add meg a felső számot!\t'))
    also  = float(input('Add meg az alsó számot!\t'))
    lista = keres(felso, also)
    if felso == 0 or also == 0:
        mehet = False
        print('Viszlát!')
    elif len(lista) == 0:
        print('Nincs ilyen szám!')
    else:
        print(f'A legalacsonyabb érték : {min(lista)}\nA legmagasabb érték: {max(lista)}')
        print(f'A legmagasabbal osztva: {felso/max(lista):.1f}/{also/max(lista):.1f}')

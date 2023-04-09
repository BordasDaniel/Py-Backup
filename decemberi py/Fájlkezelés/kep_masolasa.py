# Bináris fájl olvasása majd tartalmának másolása
# Két lehetőség van:
# 1.: egy az egyben beolvasom a bináris fájlt és utána kiirom ennek viszont meglehet annak a hátránya hogy ha nagyon
# nagy a bináris állomány ez memória túlcsorduláshoz vezethet, a program lefagy
# 2.: Ezért inkább érdemes azt az elvet követni hogy kisebb darabokat olvasok be és utána ezeket a darabokat egybe ki is irom.
# A .read() metódusnál meglehet adni hogy mennnyi bájtot olvasson be


with open('./adatok/kep.jpg', 'rb') as eredeti:
    with open('./adatok/masolat.jpg', 'wb') as masolat:
        darab_meret = 4096
        darab = eredeti.read(darab_meret)
        while len(darab) > 0:
            masolat.write(darab)
            darab = eredeti.read(darab_meret)

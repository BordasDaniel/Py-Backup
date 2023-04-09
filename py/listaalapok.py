honapok = ["Január",'február','március',"április"]
szamok = [1,2,3,4]
print(szamok)
print(honapok)
print((', ').join(honapok)) #join függvény a lista elemek közé vág be. 
print(('|').join(honapok)) 
print(len(honapok)) #len függvény fogalma az hogy hány elem tartozik a listába.
print(honapok[0]) #Index alapján lehet hivatkozni egyes lista elemekre. Az elemek indexei 0-tól kezdődnek a végtelenig. pl. ['Jan','Feb','Mac','Jun',] indexei : [0,1,2,3] lesznek.
print(honapok[3]) #pl.
print(honapok[1:3]) #A ":" egy intervallumot jelöl (Első zárt második nyitott avagy nincs benne)
print(honapok[0:2]) #pl
print(honapok[:2]) #Ha nem adok meg számot az elejére akkor automatikusan az elejétől fogja kiirni 
print(honapok[2:]) #Ha a végén nem adok meg akkor meg automatikusan a végéig fogja kiirni.
print(honapok[-2]) #Ha negativ értéket adok meg akkor a végétől fog vissza számolni, viszont már nem 0-tól hanem -1-től -végtelenig.

szo = "alma"
print(szo[1]) #Minden ugyanúgy múködik a sima szavaknál is.
print(len(szo))


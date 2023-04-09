szamok = [1, 2, 3, 4, 5]
print(list(filter(lambda szam: szam%2 !=0, szamok)))
print([szam for szam in szamok if szam%2 != 0]) #Lista értelmezéssel (list comprehension)

#Összehasonlitó operátorok
'''
== egyenlő
!= nem egyenlő
< kisebb
> nagyobb
<= kisebb vagy egyenlő
>= nagyobb vagy egyenlő
'''
# a = 15
# b = 3

# if a != b:
#     print("A két szám nem egyenlő!")


#Logikai operátorok
'''
and - és
or  - vagy
not - nem 
'''

'''
x = 5
y = -3

if x < 0 and y < 0:
    print("Mind a 2 szám negativ!")
if x < 0 or y < 0:
    print("Van közöttük negativ szám!")
if not x <= 0: 
    print("x pozitiv szám")
'''

szam = int(input("Add meg a számot amire gondoltál! "))
# if szam %2 == 0 and szam > 0:
#     print("A szám amire gondoltál pozitiv és páros")
# else: 
#     print("A szám amire gondoltál negativ és páratlan")

if szam %2 == 0:
    print("A számod páros")
else:
    print("A számod páratlan")
if szam > 0:
    print("A számod pozitiv")
else:
    print("A számod negativ")



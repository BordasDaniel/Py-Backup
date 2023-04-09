def festek_kalkulator(x,y):
   return x*y*0.13


szelesseg = float(input('Add meg a fal szélességét! '))
magassag = float(input('Add meg a fal szélességét! '))

liter = festek_kalkulator(szelesseg,magassag)
ar = liter * 700
print('A fel festéséhez kb. ' + f'{float(liter):.2f}' + ' liter festékre lesz szükség')
print(f'{ar:.0f}' + ' forintba fog kerülni')
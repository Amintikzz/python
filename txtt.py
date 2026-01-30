f = open('txtt.txt', 'r')

t = f.read().split()

print(t)
summa = int(t[0])
valuta1 = t[1]
valuta2 = t[2]

if valuta1 == 'tg' and valuta2 == 'rub':
    print(summa/5)
elif valuta1 == 'tg' and valuta2 == 'dollar':
    print(summa/500)
elif valuta1 == 'tg' and valuta2 == 'euro':
    print(summa/600)
elif valuta1 == 'rub' and valuta2 == 'tg':
    print(summa*5)
elif valuta1 == 'rub' and valuta2 == 'dollar':
    print(summa/80)
elif valuta1 == 'rub' and valuta2 == 'euro':
    print(summa/100)
elif valuta1 == 'dollar' and valuta2 == 'tg':
    print(summa*500)
elif valuta1 == 'dollar' and valuta2 == 'rub':
    print(summa*80)
elif valuta1 == 'dollar' and valuta2 == 'euro':
    print(summa/1.14)
elif valuta1 == 'euro' and valuta2 == 'tg':
    print(summa*600)
elif valuta1 == 'euro' and valuta2 == 'rub':
    print(summa*90)
elif valuta1 == 'euro' and valuta2 == 'dollar':
    print(summa*1.14)






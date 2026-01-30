import random
print('Камень ножницы или бумага?')
a = input()

a1 = 'Ножницы'
a2 = 'Бумага'
a3 = 'Камень'

comp = print(random.choice([a1,a2,a3]))
print(comp)
if a == a1 and comp == a2:
    print('Horosh')
elif a == a2 and comp == a3:
    print('Horosh')
elif a == a3 and comp == a1:
    print('Horosh')
elif a == a1 and comp == a1:
    print('Draw')
elif a == a2 and comp == a2:
    print('Draw')
elif a == a3 and comp == a3:
    print('Draw')
elif a == a1 and comp == a3:
    print('Chort')
elif a == a2 and comp == a1:
    print('Chort')
elif a == a3 and comp == a2:
    print('Chort')
    

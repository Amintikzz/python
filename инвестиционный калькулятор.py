import math
print('стартовый капитал:')
P = int(input())
print('ежемесячный взнос:')
PMT = int(input())
print('годовая ставка (в виде 0.1 = 10%):')
r = int(input())/100
n = 12
print('срок:')
t = int(input())
print('1.Год 2.Месяц')
ym = int(input())
if  ym == 1:
    A = P*(1+r/n)**(n*t)+PMT*(((1+r/n)**(n*t)-1)/(r/n))
    N = (PMT*n*t)
    M = (A - N)-P
    print('Сумма всех пополнений:', N)
    print('Доход:', M)
    print('Итоговая сумма:', A)
else:
    A = P*(1+r/n)**t+PMT*(((1+r/n)**t-1)/(r/n))
    N = (PMT*t)
    M = (A - N)-P
    print('Сумма всех пополнений:', N)
    print('Доход:', M)
    print('Итоговая сумма:', A)

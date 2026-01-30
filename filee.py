n = int(input('Введите число:'))
f = open('text.txt', 'w')
for i in range(1,n):
    if i%2 != 0:
        f.write(str(i)+ ' \n')
f.close()



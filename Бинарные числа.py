n = int(input())
otvet=False
for i in range(n):
    if n==2**i:
        otvet=True
        break
if otvet == False:
    print('NO')
else:
    print('YES')
    
    



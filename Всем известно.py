a = input()
k = True
for i in range(0,len(a)):
    if a[i] == '0':
        k = False
        break
if k == False:
    print('NO')
else:
    print('YES')
    
    
 

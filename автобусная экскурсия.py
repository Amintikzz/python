a = int(input())
n = input().split()
k = 0
crash = False


for i in range(len(n)):
    if int(n[i]) <= 437:
        k = i
        crash = True
        break

if crash:   
    print('Crash', k+1)
else:
    print('No crash')

        
    
    

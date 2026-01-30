import math
n = int(input())
x = input().split()
a = []
for i in x:
    a.append(int(i))
a.sort()

sum1 = 0
sum2 = 0

for i in range(len(a)//2):
    sum1+=a[i]

for i in range(len(a)//2, len(a)):
    sum2+=a[i]
    
print(abs(sum2-sum1))




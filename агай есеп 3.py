import math
a,b,c = map(int,input().split())
D = b**2 - 4*a*c
x1=(-1*b + math.sqrt(D))/(2*a)
y = x1**2
print(y)

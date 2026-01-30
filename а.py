a,b,c = map(int,input().split())
min1 = 0
if a<=b and a<=c:
    min1 = a
elif b<=a and b<=c:
    min1 = b
elif c<=a and c<=b:
    min1 = c
max1 = 0
if a>=b and a>=c:
    max1 = a
elif b>=a and b>=c:
    max1 = b
elif c>=a and c>=b:
    max1 = c
print(max1 - min1)



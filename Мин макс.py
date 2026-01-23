a,b,c = map(int,input().split())
max1 = 0
if a>=94 and a<=727 and b>=94 and b<=727 and c>=94 and c<=727:
    if a>=b and a>=c:
        max1 = a
    elif b>=a and b>=c:
        max1 = b
    elif c>=a and c>=b:
        max1 = c
    print(max1)
else:
    print("Error")




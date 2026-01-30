d = int(input())
b = bin(d)
c=b[2:]
s = 0
for i in range(len(c)):
    if c[i] == '1':
        s+=1
print(s)

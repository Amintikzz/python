n = []
a,b,c = map(int,input().split())
N = b - a
for i in range(c+1):
    n.append(a)
    a += N
print(n[c-1])


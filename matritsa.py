import random
n = []
for i in range(4):
    k =[]
    for j in range(4):
        a = random.randint(1,10)
        k.append(a)
    n.append(k)

for i in range(4):
    for j in range(4):
        print(n[i][j], end = ' ')
    print()


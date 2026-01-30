import random
f = open('www.txt','w')
for i in range(1,5):
    a = random.randint(1,5)
    f.write(str(a)+ ' ')
f.close()

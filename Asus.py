f=open('Asus.txt','w')
S=0
for i in range(100):
    if i%3==0:
        f.write(str(i)+', ')
f.close()    

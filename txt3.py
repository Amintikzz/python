f=open('txt2.txt','r')
t=f.read()
f.close()

print(t)
a,b=map(int,t.split())
print(a+b)

f=open('txt2.txt','a')
f.write('\n'+str(a+b))
f.close()



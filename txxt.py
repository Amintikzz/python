f = open('txxt.txt', 'r')
t = f.read()
a,b = map(int,t.split())
f.close()

f = open('txxt.txt', 'a')
f.write('\n +: ' + str(a+b))
f.write('\n *: ' + str(a*b))
f.write('\n /: ' + str(a//b))
f.write('\n -: ' + str(a-b))
f.close()


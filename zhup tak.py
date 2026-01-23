n = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
zhup = []
tak = []
for i in range(4):
    for j in range(4):
        if n[i][j]%2 == 0:
            zhup.append(n[i][j])
        else:
            tak.append(n[i][j])
print('tak: ',tak)
print('zhup: ',zhup)

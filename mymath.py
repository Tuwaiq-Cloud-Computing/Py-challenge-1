a = [5,6,10,6,6,4,10000,000,0,00,1,2,3,8]

temp = []
zeros = []

for i in range(len(a)):
    if a[i] !=0:
        temp.append(a[i])
    else:
        zeros.append(a[i])

print(temp+zeros)
def myFun(list):
    temp=[]
    zero=[]
    for x in list:
        if list[x] !=0:
            temp.append(list[x])
        else:
            zero.append(list[x])
    print(temp+zero)


myFun([1,0,2,0,3,0,4,0,5])




def sortLi(list):

    for i in list:
        list.append(list.pop(list.index(0)))

    print(list)

sortLi([0,0,0,0,8,6,5,0])

sortLi([4,-8,0,9,0,5,3,0])

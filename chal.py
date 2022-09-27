listNum=[0,4,3,0,55,3,5,0,7 ]

def LastZeresList(list):  
    list.sort(reverse = True)
    print(list)
    
def strt(list):
    list1=[]
    for i in list:
        if i == 0:
            list1.append(i)
            list.remove(i)
    list1.extend(list)
    list1.reverse()
    print(list1)
            

strt(listNum)
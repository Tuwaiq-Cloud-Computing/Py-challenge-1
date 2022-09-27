# list=[1,2,3,0,0,0]
# def func():
    
#     list.sort()
#     list.reverse()
#     print(list)
    
# func()    
list=[0,1,0,3,0,20,12]
def func(lst):
    for i in lst:
        if lst[i]==0:
            lst.pop(i)
            lst.append(0)
        return lst    
print(func(list))


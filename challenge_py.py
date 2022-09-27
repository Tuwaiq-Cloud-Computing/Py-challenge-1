
lst=[1,3,5,0,5,3,0,55,0,9,0,4,2,4]

def arrange(lst):
    
    for i in range(len(lst)):
        if lst[i]==0:
            x=lst.pop(i)
            lst.append(x)
            
        
    print(lst)
    
arrange(lst)



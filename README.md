# Py-challenge-1
Question 1:
- Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list, and finally returns the arranged list

mylist =[4,0,0,8,6,0,1,0]

def arrange(mylist):
    for i in mylist:
        if i ==0:
            mylist.remove(i)
            mylist.append(0)
    print('After rearrange list : ',mylist)

arrange(mylist)

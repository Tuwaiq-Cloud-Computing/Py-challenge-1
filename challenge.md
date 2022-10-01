


# Py-challenge-1
# Question 1:
# - Write a function that receives a list containing different numbers, 
# rearranges the list so that the zeros are the end of the list, 
# and finally returns the arranged list

Newlist=[9,8,7,0,6,0,5,0,0]
def range(Newlist):  
       for i in Newlist:
        if i ==0:
            Newlist.remove(i)
            Newlist.append(0)
       print('After range list : ',Newlist)

range(Newlist)

# for i in range(len(Newlist)):
# if Newlist[i] < 1:
# Z=Newlist.pop(i)
# Newlist.append(Z)






# Py-challenge-1
Question 1:
- Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list, and finally returns the arranged list
a= [7,5,8,0,2,0,5,0,1]
n = len(a)

def f1(a,n):
 j = 0
 for i in range(n):
    if a[i] != 0:
        a[j], a[i] = a[i], a[j]  
        j += 1
 print(a) 
f1(a,n)

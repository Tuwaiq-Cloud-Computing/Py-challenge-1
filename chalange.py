# list[3,6,3,7,9,0,2,0,2,9,]

# def arrange1(list):

#     for i in list:
#         if i==0:
#          list.append(0)
#          print(list)
list=[2,5,0,4,8,3,0,1,8,9,0,4,9,7]
def arrange1(list):
   
    #list=[2,5,0,4,8,3,0,1,8,9,0,4,9,7]
    for i in list:
        if i==0:
            list.remove(i)
            list.append(0)
    print(list) 
      

arrange1(list)

# 1 4 12 32 80

# 1 2 3 4 5 6
# 1 4 12     

# 

# for i in range(5):

# n=1
# for i in range(5):
#     for j in range(i+1):
#         n+=1
#         print(n,end=" ")
#     print()
    # n+=1
    # n+=i
# for i in range(1,6):
#     for j in range(1,6): 
#         print(i,j,end=" ")
#     print()

# for i in range(6): #ROW
#     for j in range(i): #Column
#         print("*",end=" ")
#     print()

# for i in range(5,0,-1): #ROW
#     for j in range(i): #Column
#         print("*",end=" ")
#     print()


# i=1
# while i<=5 :
#     print(i,end=" ")
#     i+=1
# print()

# i=5
# while i>=1 :
#     print(i,end=" ")
#     i-=1

# i=1
# while i<=5 :
#     j=1
#     while j<=i :
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1
# print("\n i : ",i)


# i=1
# while True:   
#     print(i)  
#     if(i>=10):  
#         break   
#     i+=1 

# i=1
# while i<=5 :
#     print(i,end=" ")
#     i+=1
# print()

# 15/12

# list1 = ['physics', 'chemistry']
# # # print(list1)
# # print(list1[1])

# list2 = [1, 2, 3, 4, 5 ]
# list3 = ["a", "b", "c", "d"]
# list4 =['pooja',"jalpa"]
# print("\n Length of list1 is",len(list1))
#for + operator in list
# print(list1+list2)
# print(list1)

##print(ls)
# ####for * operator in list
# print(['hi']*4)
# print(list4 * 2)
# print(list4[0] * 2)

# print(list3 * 2)
# print(list2)


# list1 = [ 'chemistry','physics','Math','physics']
# list2 = ['Math']
# list1.append(list2)
# list1.append('Math')
# print(list1)
# list1.pop()
# list1.remove('physics')
# print(list1)

# square = []
# for i in range(1,10):
#     square.append(i**2)
# print(square)

# 17/12

# import array as ar
# a = ar.array('i',[1,2,3,4])
# b = ar.array('i',[4,3,2,1])
# print(a)

# print(a*2)
# for i in range(4):
#     print(a[i],end=" ")
#     print(b[i],"\t")

# for i in a:
#     print(i)
# for i in b:
#     print(i)

# from datetime import datetime
# before = datetime.now()
# k=0
# for i in range(4):
#     k+=a[i]*b[i]
# print (k)
# after = datetime.now()

# print  ("time : ", after - before )
# print("Before : ", before)
# print("after : ",after)  

## 18/12

# n=5
# for i in range(1,n+1):
#     print("*"*i)

# print("*"*3)
# print("*"*2)


# import array as ar
# a1 = ar.array('i',[1,2,3,4])
# print(a1)
# print(type(a1))
# import numpy as np
# from datetime import datetime
# a = np.array([1, 2, 3,4])
# b = np.array([4,3,2,1])
# before = datetime.now()
# print("a dot b : ",np.dot(a,b))
# after = datetime.now()


# import array as ar
# a = ar.array('i',[1,2,3,4])
# b = ar.array('i',[4,3,2,1])
# before = datetime.now()
# k=0
# for i in range(4):
#     k+=a[i]*b[i]
# print (k)
# after = datetime.now()
# print  ("time : ", after - before )

# 20/12

# import numpy as np
# a = np.array([10,20,30,40])
# l = [10,20,30,40]
# print(a,end=" ")
# print(a*2,end=" ")
# print(a+5,end=" ")
# b = np.array([a*2,a+2])
# print(type(b))

# print(a*2)
# print(a/2)

# print(type([a]))
# print(type(a))
# l = [a,a*2,a+5]
# print(l)
# print(l[0])
# print(a[0])

# import numpy as np
# import sys
# l = [10,20,30,40,50,60,70,80,90,100,10,20,30,40,50,60,70,80,90,100]
# a = np.array([10,20,30,40,50,60,70,80,90,100,10,20,30,40,50,60,70,80,90,100])
# print('The Size of list l => ',sys.getsizeof(l))
# print('The Size of ndarray a => ',sys.getsizeof(a))


# import numpy as np
# import time
# import sys
# SIZE =100
# l1 = range(SIZE)
# l2 = range(SIZE)
# a1 = np.arange(0,SIZE,0.333)
# a2 = np.arange(10)
# print(l1)
# print(type(a1))
# print(a1)
# print(a2)

# result = a1 + a2
# print(result)

# import numpy as np
# a = np.ones([2,3])
# print(a)
# print(type(np.ones([2,3])))


# import numpy as np
# a = np.linspace(2.0, 3.0, num=5)
# print(3+3)

# git remote add origin https://github.com/Qodeskill/ml_9.00am.git
import numpy as np
# import matplotlib.pyplot as plt
# a = np.arange(1,11)
# print('a ==> {a}')
# print(f'a ==> {a}')
# print(f'dimensions of the array a ==> {a.ndim}')
# print(f'data type of elements of array a ==> {a.dtype}')
# print(f'size of the array a ==> {a.size}')
# print(f'shape of the array a ==> {a.shape}')

# a = np.arange(1,10).reshape(3,3)
# print(f"Original 2-D array ==> \n {a}")
# print(f'dimensions of the array a ==> {a.ndim}')
# print(f"Elements prsent at 0-diagonal ==> {np.diag(a,k=0)}")
# print(f"Elements prsent at 1-diagonal ==> {np.diag(a,k=1)}")
# print(f"Elements prsent at 2-diagonal ==> {np.diag(a,k=2)}")
# print(f"Elements prsent at -1-diagonal ==> {np.diag(a,k=-1)}")
# print(f"Elements prsent at -2-diagonal ==> {np.diag(a,k=-2)}")
# print(f"Elements prsent at 3-diagonal ==> {np.diag(a,k=3)}")
# a = np.array([10,20,30,40])
# print(f'dimensions of the array a ==> {a.ndim}')
# print(" array ")
# print(np.diag(a,k=2))
# print(np.diag(a,k=2))
# s = np.random.uniform(20,30,size=1000000)

# a = np.array([10,20,30,40,50])
# print(a[4])
# print(a[-1])

# a = np.array([[10,20,30],[40,50,60]])
# print(f"Shape of the array a : {a.shape}")
# print("To Access the element 50")
# print(f"a[1][1] ==> {a[1][1]}")
# print(f"a[1][-2] ==> {a[1][-2]}")
# print(f"a[-1][2] ==> {a[-1][-2]}")
# print(f"a[-1][1] ==> {a[-1][1]}")


# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(f"Shape of the array a : {a.shape}")

# print(f"a[1][-1] ==> {a[1][-1]}")
# print(f"a[-2][-1] ==> {a[-2][-1]}")
# print(f"a[-2][2] ==> {a[-2][2]}")


l = [[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]]
# print(type(l))
a = np.array(l)
# print(type(a))

# print(f'dimensions of the array a ==> {a.ndim}')
# print(f"Shape of the array a ==> {a.shape}")
# print(a)
# print("To access the element 14 from the 3-D array")
print(f"a[0][0][1] ==> {a[1][2][1]}")
# print(f"a[-1][-2][-2] ==> {a[-1][-2][-2]}")
# print(f"a[1][-2][-2] ==> {a[1][-2][-2]}")
# print(f"a[-1][1][-2] ==> {a[-1][1][-2]}")


# view
# a = np.array([10,20,30,40])
# b = a.view()
# print(f"Original Array(a) ==> {a}")
# print(f"View of the Array(b) ==> {b}")
# print("*"*80)
# print("Changing the values of a, it will reflect to view(b) also :")
# a[0]=7777
# print(f"Changed Array(a) ==> {a}")
# print(f"View of the Array(b) ==> {b}")
# print("*"*80)
# print("Changing the values of view(b), it will reflect to a also :")
# b[-1]=999
# print(f"Changed view Array(b) ==> {b}")
# print(f"Original Array(a) ==> {a}")



# copy

# a = np.array([10,20,30,40])
# b = a.copy()
# print(f"Original Array(a) ==> {a}")
# print(f"copy of the Array(b) ==> {b}")
# print("*"*60)
# print("Changing the values of a, it will not reflect to copy(b) ")
# a[0]=7777
# print(f"Changed Array(a) ==> {a}")
# print(f"copy of the Array(b) ==> {b}")
# print("*"*60)
# print("Changing the values of copy(b), it will not reflect to a ")
# b[-1]=999
# print(f"Changed copy Array(b) ==> {b}")
# print(f"Original Array(a) ==> {a}")


# to know the position of an element in the array
# np.where(a==88)

# Slicing ==> group of elements which are in order

# l = [10,20,30,40,50,60,70]
# l[2:6] 


# l[-6:-2]

# If we are not specifying begin index then default is 0
# l[:3] 

# l[2:] # from 2nd index to last


# l = [10,20,30,40,50,60,70,80,90]
# l[2:6:2] # from 2nd index to 6-1 index with step 2


# a = np.arange(10,101,10)
# a[2:5] # from 2nd index to 5-1 index

# a[::1] # entire array

# Slice operator on 2-D numpy array

# a = np.array([[10,20],[30,40],[50,60]])
# a = np.array([[10,20],[30,40],[50,60]])
# b = a[0,:] # row is in index form, it will return 1-D array
# c = a[0:1,:] # it will return 2-D array
# print(f"The dimension of b : {b.ndim} and the array b : {b} ")
# print(f"The dimension of c : {c.ndim} and the array c : {c} ")

# print(f"a[0:2,1:2] value is : \n {a[0:2,1:2]}")
# print(f"a[:2,1:] value is : \n {a[:2,1:]}")

# print(f"a[0::2,:] value is : \n {a[0::2,:]}")
# print(f"a[::2,:] value is : \n {a[::2,:]}")



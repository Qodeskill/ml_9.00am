import numpy as np
# Sorting elements of nd arrays
# • We can sort elements of nd array.
# • numpy module contains sort() function.
# • The default sorting algorithm is quicksort and it is Ascending order
# • We can also specify mergesort, heapsort etc
# • For numbers-->Ascending order
# • For Strings-->alphabetical order

# a = np.array([70,20,60,10,50,40,30])
# sorted_array = np.sort(a)
# sorted_array = np.sort(a)[::-1] #descending order
# print(f"Original array a : {a}")
# print(f"Original array a : {sorted_array}")

# How to insert elements into ndarray
# • insert() ==> inserting the element at the required position
# • append() ==> inserting the element at the end
# a = np.arange(10)
# b = np.insert(a,2,7777)
# print(f"array a : {a}")
# print(f"array b : {b}")


# b = np.insert(a,[2,5],7777)
# print(f"array a : {a}")
# print(f"array b : {b}")


# b = np.insert(a,[2,5,7],[7777,8888])
# print(f"array a : {a}")
# print(f"array b : {b}")

# a = np.array([[10,20],[30,40]])
# b = np.insert(a,1,100,axis=0)
# c = np.insert(a,1,100,axis=-2)
# print(f"array a :\n {a}")
# print(f"array b :\n {b}")
# print(f"array c :\n {c}")

# We can delete elements of ndarray by using delete() function.
# delete(arr, obj, axis=None)
# • obj can be int, array of ints or slice
# • for multi-dimensional arrays we must have to specify the axis, other-wise the
# default axis=None will be considered. In this case first the array is flatten to the 1-D
# array and deletion will be performed

# a = np.arange(10,101,10)
# b = np.delete(a,3) # delete element at 3rd index
# print(f"array a : {a}")
# print(f"array b : {b}")

# b = np.delete(a,[0,4,6]) # delete elements  at indices:0,4,6
# print(f"array a : {a}")
# print(f"array b : {b}")

a = np.arange(1,13).reshape(4,3)
# b = np.delete(a,np.s_[0:3],axis=0) # rows from index-0 to index-(3-1) will be deleted
# print(f"array a : \n {a}")
# print(f"array b : \n {b}")

b = np.delete(a,np.s_[::2],axis=0) # to delete every 2nd row (alternative row) from index-0
print(f"array a : \n {a}")
print(f"array b : \n {b}")

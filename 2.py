
import numpy as np
# a = np.arange(10,51,10)
# print(a)
# for x in a:
#     print(x)

# Iterate elemetns of 2-D array

# a = np.array([[10,20,30],[40,50,60],[70,80,90]])
# for x in a:
#     for y in x:
#         print(y)

# Iterate elemetns of 3-D array

# a = np.array([[[10,20],[30,40]],[[50,60],[70,80]]])
# print(a.shape)
# print(a)
# for x in a: 
#  for y in x:
#     for z in y: 
#         print(z)


# By using nditer() function
# Advantage: To iterate any n-D array only one loop is enough.
# • nditer is a class present in numpy library.
# • nditer() ==> Creating an object of nditer class.

# a = np.arange(10,51,10)
# for x in np.nditer(a):
#  print(x)

# a = np.array([[10,20,30],[40,50,60],[70,80,90]])
# for x in np.nditer(a):
#  print(x)

# a = np.array([[10,20,30],[40,50,60],[70,80,90]])
# for x in np.nditer(a,flags=['buffered'],op_dtypes=['float']):
#  print(x)
# print(a)

# •By using nditer() we will get elements only but not indexes
# • If we want indexes also in addition to elements, then we should use
# ndenumerate() function.
# • ndenumerate() function returns multidimensional index iterator which yields
# pairs of array indexes(coordinates) and values.

# a = np.array([10,20,30,40,50,60,70])
# a = np.array([[10,20,30],[40,50,60],[70,80,90]])
# a = np.arange(1,25).reshape(2,3,4)

# 29/12

# a = np.array([10,20,30,40,50,60,70])
# a = np.array([[10,20,30],[40,50,60],[70,80,90]])
# for pos,element in np.ndenumerate(a):
#     print(f'{element} element present at index/position:{pos}')

# Arithmetic Operators:
# • Addition :: +
# • Subtraction :: -
# • Multiplication :: *
# • Division :: /
# • Floor Division :: //
# • Modulo operation/Remainder Operation :: %
# • Exponential operation/power operation :: **

# • The result of division operator(/) is always float.
# • But floor division operator(//) can return either integer and float values.
# • If both arguments are of type int, then floor division operator returns int value only.
# • If atleast one argument is float type then it returns float type only

# a = np.array([10,20,30,40])
# a = np.array([[10,20,30],[40,50,60],[70,80,90]])
# a = np.arange(1,25).reshape(2,3,4)

# print(f"a+2 value is :: {a+2}")
# print(f"a-2 value is :: {a-2}")
# print(f"a*2 value is :: {a*2}")
# print(f"a**2 value is :: {a**2}")
# print(f"a/2 value is :: {a/3}")
# print(f"a//2 value is :: {a//3}")

# ZeroDivisionError
# • In python Anything by zero including zero/zero also results in : ZeroDivisionError
# • But in numpy there is no ZeroDivisionError
# • 10/0 ==> Infinity(inf)
# • 0/0 ==> undefined(nan--->not a number)

# print(f"The value of 10/0 :: {10/0}")
# print(f"The value of 0/0 :: {0/0}")

# a = np.arange(6)
# print(f"The value of a/0 :: {a/0}")

# Arithmetic operators for Arrays with Arrays (Arrays with Arrays):
# To perform arithmetic operators between numpy arrays, compulsory both arrays
# should have
# • same dimension,
# • same shape and
# • same size,

# a = np.array([1,2,3,4])
# b = np.array([10,20,30,40])

# a = np.array([[10,20,30],[40,50,60],[70,80,90]])
# b = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(f"Dimension of a : {a.ndim}, size of a :{a.shape} and shape of a : {a.shape}")
# print(f"Dimension of b : {b.ndim}, size of a :{b.shape} and shape of a : {b.shape}")
# print(f"a array :: {a} and b array :: {b}")
# print(f"a+b value is :: {a+b}")
# print(f"a-b value is :: {a-b}")
# print(f"a*b value is :: {a*b}")
# print(f"a**b value is :: {a**b}")
# print(f"a/b value is :: {a/b}")
# print(f"a//b value is :: {a//b}")

# a = np.array([10,20,30,40])
# b = np.array([10,20,30,40,50])
# print(f"Dimension of a : {a.ndim}, size of a :{a.shape} and shape of a : {a.shape}")
# print(f"Dimension of b : {b.ndim}, size of a :{b.shape} and shape of a : {b.shape}")
# print(f"a+b value is :: \n {a+b}")


# a = np.array([10,20,30])
# b = np.array([40])
# print(f"Shape of a : {a.shape}")
# print(f"Shape of b : {b.shape}")
# print(f"a+b : {a*b}")

# 30/12

# --Broadcasting 
# https://www.youtube.com/watch?v=tuKHsfAehz4

# • Generally Arithmetic operations are performed between two arrays are having
# same dimension, shape and size.
# • Eventhough dimensions are different,shapes are different and sizes are different
# still some arithmetic operations are allowed by Broadcasting
# • Broadcasting will be performed automatically by numpy itself and we are not
# required to perform explicitly.
# • Broadcasting won't be possible in all cases.
# • Numpy follow some rules to perform Broadcasting. If the rules are satisfied then
# only broadcasting will be performed internally while performing arithmetic
# operations.

# --Note

# • If both arrays have same dimension, same shape and same size then broadcasting is
# not required.
# • Different dimensions or different shapes or different sizes then only broadcasting is
# required.

# Rule-1: Make sure both arrays should have same dimension
# • If the two arrays are of different dimensions, numpy will make equal dimensions.
# Padded 1's in the shape of lesser dimension array on the left side, until both arrays
# have same diemension
# Eg: Before
# • a array has shape :: (4,3) ----> 2-D array
# • b array has shape :: (3,) ----> 1-D array
# After
# • Both arrays a and b are different dimensions.
# • By Rule-1 Numpy will add 1's to the lesser dimension array(b).
# Now the array a is ----> (4,3)
# and the array b becomes ::: (1,3) -- By using Rule-1
# • Now Both arrays are in same dimension array a:: 2-D and array-b :: 2-D
# a array has shape :: (4,3) ----> 2-D array
# b array has shape :: (1,3) ----> 2-D array

# # Rule-2:
# • If the size of two arrays does not match in any dimension, then the arrays with size
# equal to 1 in that dimension will be increased to size of other dimension to match
# Eg:
# • From Rule-1 we got a ==> (4,3) and b ==> (1,3)
# • Here first co-ordinate of a => 4 and b => 1. Sizes are different
# • According to Rule-2 the array with size 1 (here arrray b with size 1) will be
# increased to 4 (corresponding size of array a).
# • Second co-ordinate of a => 3 and b => 3. Sizes are matched.
# • After applying Rule-2 the dimensions of a and b are changed as follows
# a array has shape ==> (4,3) ====> 2-D array
# b array has shape ==> (4,3) ====> 2-D array
# • Now both the arrays are having same dimension, shape and size. So we can perform
# any arithmetic operations

# a = np.array([10,20,30,40])
# b = np.array([1,2])
# print(a+b)


# a = np.array([10,20,30])
# b = np.array([40])

# a = np.arange(15).reshape(3,5)
# b = np.arange(5)
# print(f"Shape of a : {a.shape} and Dim of a : {a.ndim}")
# print(f"Shape of b : {b.shape} and Dim of b : {b.ndim}")
# print(a)
# print(b)

# a = np.arange(3)
# b = np.arange(3).reshape(3,1)
# print(f"Shape of a : {a.shape} and Dim of a : {a.ndim}")
# print(f"Shape of b : {b.shape} and Dim of b : {b.ndim}")
# print(a)
# print(b)

# print(a+b)

# print(f"Shape of a : {a.shape}")
# print(f"Shape of b : {b.shape}")
# print(f"a+b : {a+b}")

# new Commit 3012 852pm
# 31/12

# a = np.arange(9).reshape(3,3)
# b = np.resize(a,(5,2))
# print(f"Original array : {a}")
# print(f"Reshaped array :\n {b}")

# a = np.arange(6).reshape(3,2)
# b = a.flatten('F') # F fortarn style
# b = a.flatten() #c lng style
# print(f"Original array :\n {a}")
# print(f"Flatten array :\n {b}")

# import numpy as np
# a = np.arange(9).reshape(3,3)
# # atrans = np.transpose(a)
# atrans = np.transpose(a,axes=(1,0))
# atrans1 = np.transpose(a,axes=(-1,0))
# print(f"Original Array : \n {a}")
# # print(f"Transposed Array : \n {atrans}")
# print(f"Transposed Array : \n {atrans1}")

# a = np.arange(1,7).reshape(2,3)
# atrans = np.transpose(a)
# atrans = np.transpose(a,axes=(0,1))
# print(f"Original Array : \n {a}")
# print(f"Transposed Array : \n {atrans}")
# print(f"Original Array shape : {a.shape}")
# print(f"Transposed Array shape: {atrans.shape}")

# a = np.arange(1,7).reshape(2,3)
# atrans = np.transpose(a,axes=(0,1))
# print(f"Original Array : \n {a}")
# print(f"Transposed Array : \n {atrans}")
# print(f"Original Array shape : {a.shape}")
# print(f"Transposed Array shape: {atrans.shape}")

# a= np.arange(16).reshape((2, 2, 4))
# atrans = np.transpose(a)
# print(f"Original Array : \n {a}")
# print(f"Transposed Array : \n {atrans}")
# print(f"Original Array shape : {a.shape}")
# print(f"Transposed Array shape: {atrans.shape}")

# a= np.arange(1,28).reshape((3,3, 3))
# atrans = np.transpose(a)
# print(f"Original Array : \n {a}")
# print(f"Transposed Array : \n {atrans}")
# print(f"Original Array shape : {a.shape}")
# print(f"Transposed Array shape: {atrans.shape}")

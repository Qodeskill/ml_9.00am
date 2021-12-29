
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


a = np.array([10,20,30])
b = np.array([40])
print(f"Shape of a : {a.shape}")
print(f"Shape of b : {b.shape}")
print(f"a+b : {a*b}")





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


By using nditer() function
Advantage: To iterate any n-D array only one loop is enough.
• nditer is a class present in numpy library.
• nditer() ==> Creating an object of nditer class.

a = np.arange(10,51,10)
for x in np.nditer(a):
 print(x)

# a = np.array([[10,20,30],[40,50,60],[70,80,90]])
# for x in np.nditer(a):
#  print(x)

# a = np.array([[10,20,30],[40,50,60],[70,80,90]])
# for x in np.nditer(a,flags=['buffered'],op_dtypes=['float']):
#  print(x)
# print(a)

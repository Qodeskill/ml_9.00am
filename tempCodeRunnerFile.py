
a = np.array([3,5,7,6,7,9,4,6,10,15])
b = np.where( a%2 == 0, 'even', 'odd')

print(f"element { b} is {a} " )

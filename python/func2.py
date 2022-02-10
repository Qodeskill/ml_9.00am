#Required arguments are the arguments passed to a function in correct 
#positional order. Here, the number of arguments in the function call 
#should match exactly with the function definition.
# To call the function printme(), you definitely need to pass one argument, otherwise it gives a syntax error as follows −

# print("1")
# def printme(str):
#    "This prints a passed string into this function"
#    print (str)
#    return ;


print("1")
def printme(str):
   "This prints a passed string into this function"
   print (str)
   return len(str) #it return length of str ;
s1 = "hi"
print("2")
# s2 = " how are you"
print(printme(str="Hello"))
print("3")
printme(s1)
print("4")

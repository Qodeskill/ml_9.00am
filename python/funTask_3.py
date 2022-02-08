str = "garvit"
def myString(str):
    arr=[]
    n = len(str)
    # print(str," - ",n)
    for i in range(0,n):
        for j in range(i,n):
            arr.append(str[i:(j+1)])
    print(arr)
myString(str)
myString("DEll")
myString("Dog")
myString("surat")
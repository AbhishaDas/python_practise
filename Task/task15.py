def getArray(array,size):
    print("Enter the values: ")
    for i in range(size):
       values= int(input())
       array.append(values)
    

def displayArray(array):
    print("Array: ", end=" ")
    for i in array:
        print(i, end=" ")
    print()

array=[]
size=int(input("Enter the size of an array: "))
getArray(array,size)
displayArray(array)

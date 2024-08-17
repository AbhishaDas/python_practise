size=int(input("Enter the size of an array: "))
print("Enter the values of array: ")

array_values=[]
for i in range(size):
    values=int(input())
    array_values.append(values)

array_values.sort(reverse=True)
print("Sorted array: ",array_values)

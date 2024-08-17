size=int(input("Enter the size of an array: "))
print("Enter the values of the array: ")

array=[]
for i in range(size):
    values=int(input())
    array.append(values)

array_even=[]
for i in array:
    if i%2==0:
        array_even.append(i)

print("Number of even numbers in the given array is",len(array_even))


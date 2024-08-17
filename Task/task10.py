size=int(input("Enter the size of the array: "))

Array1 =[]
for i in range(size):
    values=int(input("Enter the values of Array 1: "))
    Array1.append(values)

Array2 =[]
for i in range(size):
    values=int(input("Enter the values of Array 2: "))
    Array2.append(values)

temp= []

temp = Array1
Array1=Array2
Array2=temp

print("Array after swapping: ")
print("Array 1: ",Array1)
print("Array 2:",Array2)


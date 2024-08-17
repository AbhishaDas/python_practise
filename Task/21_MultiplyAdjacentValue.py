"""Write a program to multiply the adjacent values of an array and store it in an another array
Program should accept an array
Multiply the adjacent values
Store the result into another array
Eg:
Enter the array limit
5
Enter the values of array
1	2	3	4	5
Output
2	6	12	20"""



limit=int(input("Enter the array limit: "))
arr=[]
print("Enter the values of array: ")
for _ in range(limit):
    values=int(input())
    arr.append(values)

result=[arr[i]*arr[i+1]for i in range(len(arr)-1)]
print("Output: ",result)

string=str(input("Enter a String: "))
array_str=[]
for i in range(len(string)):
    array_str.append(string[i])

original_array= array_str.copy()

array_str.reverse()

if original_array==array_str:
    print("Palindrome")

else:
    print("not palindrome")
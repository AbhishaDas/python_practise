#output

"""a=10
b=20
print("First num is "+str(a),"second num is "+str(b))"""

#input
"""a=input("Enter the first num: ")
b=input("Enter the second num: ")
print("first num "+str(a)+" second num"+str(b))"""

#sum of 2 numbers
"""a=input("first num: ")
b=input("second num: ")

sum=(int(a)+int(b))

print("sum of 2 numbers: "+str(sum))"""

"""i=20
while i<=10:
    print(i)
    i=i+1
else:
    print("not \n working")"""

i = 1
while i < 4:
    j = 1
    while j < i:
        print("* ", end="")  # Print asterisk without moving to the next line
        j += 1
    print()  # Move to the next line after completing the inner loop
    i += 1




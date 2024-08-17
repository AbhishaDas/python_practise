#function
"""def myfun():
    print("Hello")

myfun()"""


#passing arguments
"""def myfun(name):
    print("My name is "+name)

myfun("Abhishadas")"""
#------------------------------------
"""def myfun(name):
    print("My name is "+name)

value="Abhi"
myfun(value)"""


#arbitary arguments
"""def myfun(*values):
    print(values)

myfun("A","B","C","D") """

#global and local variables
"""value=10     #global variable

def myfun():
    value=30    #local variable
    print(value)

myfun()
print(value)"""

#sum of 2 numbers
# with argument and with return type
"""def sum(num1,num2):
    return num1+num2


num1=int(input("Enter first num: "))
num2=int(input("Enter second num: "))
res=sum(num1,num2)
print(res)"""


# with argument without return type
"""def sum(num1,num2):
    sum=num1+num2
    print(sum)

num1=int(input("Enter first num: "))
num2=int(input("Enter second num: "))
sum(num1,num2)"""

# without argument with return type
"""def sum():
    num1=int(input("Enter first num: "))
    num2=int(input("Enter second num: "))
    return num1+num2

res=sum()
print(res)"""

# without argument without return type
"""def sum():
    num1=int(input("Enter first num: "))
    num2=int(input("Enter second num: "))
    sum=num1+num2
    print(sum)

sum()"""





fruits=["Apple","Mango","Cherry","Pineapple"]

"""print length of he list"""
# print(len(fruits))

"""access 3rd element"""
# print(fruits[2])

"""add banana"""
fruits.append("banana")
print(fruits)

"""remove last fruit"""
# fruits.pop()
# print(fruits)

"""check apple present in the list"""
# if "Apple" in fruits:
#     print("Apple present in fruits")
# else:
#     print("no apple not in list")

"""sort ascending order"""
# fruits.sort()
# print(fruits)

"""new list"""    
num=[1,2,3,4,5,6,7,8,9,10]    

"""find summ of num"""
# sum=0
# for x in num:
#     sum+=x
# print(sum)

"""largest number"""
# num.sort()
# largest=num[-1]
# print(largest)
"""--------------------"""

"""list containing sqare of 5 elements"""
# squares=[x**2 for x in range(1,6)]
# print(squares)

"""concatenate 2 list"""
concatenate_list=fruits+num
print(concatenate_list)

"""remove duplicate"""
unique_list=set(concatenate_list)
print(unique_list)

"""reverse order of fruits"""
# fruits.sort(reverse=True)
# print(fruits)

"""index of banana"""
# x=fruits.index("banana")
# print(x)





    
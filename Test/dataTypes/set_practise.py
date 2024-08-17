colors={"red","yellow","purple"}
fruits={"kiwi","apple","mango","orange"}

"""length of each set"""
# x=len(colors)
# print(x)

# x=len(fruits)
# print(x)

"""check blue present or not"""
# if "blue" in colors:
#     print("blue present")
# else:
#     print("not present")

"""add orange to colors"""
colors.add("orange")
print(colors)

"""remove "apple" from fruits"""
# fruits.discard("apple")
# print(fruits)

"""intersection of 2 sets"""
x=colors.intersection(fruits)
print(x)

"""union of 2 sets"""
x=colors.union(fruits)
print(x)

"""find elements present in set1 but not in set2"""
x=colors.difference(fruits)
print(x)

"""check if set1 is a subset of the other"""
x=colors.issubset(fruits)
print(x)

num={1,2,3,4,5}
sum=0
for x in num:
    sum+=x
print(sum)


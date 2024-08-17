fruits=["Apple","Mango","Cherry"]

#append()
fruits.append("Banana")
print(fruits)

#clear()
fruits.clear()
print(fruits)

#copy()
fruits=["Apple","Mango","Cherry"]
x=fruits.copy()
print(x)

#count()
x=fruits.count("Apple")
print(x)

#extend()
fruits1=["Banana","Kiwi","Blueberry"]
fruits.extend(fruits1)
print(fruits)

#index()
x=fruits.index("Banana")
print(x)

#insert()
fruits.insert(1,"Orange")
print(fruits)

#pop()
fruits.pop(2)
print(fruits)

#remove()
fruits.remove("Kiwi")
print(fruits)

#reverse()
fruits.reverse()
print(fruits)

#sort()
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)



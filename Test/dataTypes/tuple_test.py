fruits=("Apple","Banana","Mango","Blueberry","Apple")

#count()
x=fruits.count("Apple")
print(x)

#index()
x=fruits.index("Banana")
print(x)

#update tuple
#add an item
y=list(fruits)
y.append("Orange")
fruits=tuple(y)
print(fruits)

#remove an item
y=list(fruits)
y.remove("Blueberry")
fruits=tuple(y)
print(fruits)

#add tuple to a tuple
y=("Jackfruit","Mulberry",)
fruits+=y
print(fruits)

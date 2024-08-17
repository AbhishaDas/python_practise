#for loop
"""fruits=["Mango","Orange","Apple","Kiwi","Strawberry"]
for x in fruits:
    print(x)"""

#looping through a string
"""for x in "BANANA":
    print(x)"""

#break statement
"""fruits=["Mango","Orange","Apple","Kiwi","Strawberry"]
for x in fruits:
    print(x)

    if x=="Apple":
        break"""

#if break is before print
"""fruits=["Mango","Orange","Apple","Kiwi","Strawberry"]
for x in fruits:
    if x=="Apple":
        break

    print(x)"""

#continue statement
"""fruits=["Mango","Orange","Apple","Kiwi","Strawberry"]
for x in fruits:
    if x=="Apple":
        continue

    print(x)"""

#range function
"""for x in range(10):
    print(x)"""

"""for x in range(2,6):
    print(x)"""

"""for x in range(1,50,5):
    print(x)"""

#else statement
"""for x in range(6):
    print(x)

else:
    print("Finished")"""

"""for x in range(6):
    if x==3: break
    print(x)
else:
    print("Finished")"""

#nested loops
prop=["Tasty","Big","Fresh"]
fruits=["Apple","Mango","Banana"]

for x in prop:
    for y in fruits:
        print(x,y)
thislist=["apple","mango","kiwi","banana"]
print(thislist)
#o/p: ['apple', 'mango', 'kiwi', 'banana']

# add list item- append()
list1=thislist.append("orange")
print(thislist)
#o/p: ['apple', 'mango', 'kiwi', 'banana', 'orange']

#insert() to insert list item at a specific index
fruits=["mango","apple","orange","kiwi"]
fruits.insert(1,"pineapple")
print(fruits)
#o/p: ['mango', 'pineapple', 'apple', 'orange', 'kiwi']

#extend() append elements from another list to the current list
fruitlist=["apple","mango","kiwi","banana"]
numlist=[1,2,3,4]
fruitlist.extend(numlist)
print(fruitlist)
#o/p: ['apple', 'mango', 'kiwi', 'banana', 1, 2, 3, 4]

#remove() 
fruitlist.remove("apple")
print(fruitlist)
#o/p: ['mango', 'kiwi', 'banana', 1, 2, 3, 4]

#pop(), del() remove specific index
fruitlist1=["apple","mango","kiwi","banana"]
fruitlist1.pop(2)
print(fruitlist1)
del fruitlist1[0]
print(fruitlist1)
#o/p: ['apple', 'mango', 'banana'], ['mango', 'banana']

#clear() to empties the list
fruitlist1.clear()
print(fruitlist1)
#o/p: []

#loop list
#loop through list using for loop
listitem=["apple","mango","kiwi","banana"]
for x in listitem:
    print(x)

#loop through the index number-use range() & len() function
listitem1=["apple","mango","kiwi","banana"]
for i in range(len(listitem1)):
    print(listitem1[i])

#using while loop-len() 
listitem2=["orange","pineapple","strawberry","berry"]
i=0
while i<len(listitem2):
    print(listitem2[i])
    i=i+1

#list comprehension
[print (x) for x in listitem]

#sort list alphanumerically - sort()
veggis=['tomato','chilli','potato','onion']
list.sort(veggis)
print(veggis)

#reverse te list items
veggis.sort(reverse=True) #or veggis.reverse()
print(veggis)

#sorting is case sensitive use str.lower as a key fn
veggis.sort(key=str.lower)
print(veggis)

#copy a list
list1=['a','b','c']
list2=[1,2,3]
list2=list1.copy()
print(list2)

#append
for x in list2:
    list1.append(x) #now list2=['a],'b,'c']
    print(list1)

#join 2 ist using + operator
list3=['a','b','c']
list4=[1,2,3]
listjoin=list3+list4
print(listjoin)

#extend()
list3.extend(list4)
print(list3)


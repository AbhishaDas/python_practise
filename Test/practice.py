# str="geek quiz practice code"

# words=str.split()
# reversed_str= " ".join(reversed(words))

    
# print(reversed_str)
# """-------------------------------------------"""
# str="my name is laxmi"

# words= str.split()
# words.remove('my')

# reversed_str=' '.join(reversed(words))
# print(reversed_str)
"""----------------------------------------------"""
# inputlst=[12,35,9,56,24]

# temp=inputlst[0]
# inputlst[0]=inputlst[-1]
# inputlst[-1]=temp
# print(inputlst)
# """--------------------------------------------------"""
# inputlist=[1,2,3]
# keylist=['a','b','c']
# dict={}
# for i in range(len(inputlist)):
#     dict[keylist[i]]= inputlist[i]
# print(dict)    
"""---------------------------------------------------"""

# my_dict = {'b': 2, 'a': 1, 'c': 3}

# sorted_dict={key:my_dict[key] for key in sorted(my_dict)}
# print(sorted_dict)

# """------------------------------------------------------"""
# my_dict={'a': 1, 'b': 2, 'c': 3}

# my_dict.pop("b")
# print(my_dict)
    
# """------------------------------------------------------"""
# name=["ramu","raju","balu"]
# age=[12,34,54]

# dictn={}
# for x in range(len(name)):
#     dictn[name[x]]=age[x]
# print(dictn)
# """--------------------------------------------------------"""
# dictn={'ramu': 12, 'raju': 34, 'balu': 54}
# sorted_list={}

# newlst={name:age for name,age in dictn.items() if age>18}
# print(newlst)



dictitem={'a':2,'b':4,'c':6}

new_list={x:y/2 for x,y in dictitem.items()}
print(new_list)

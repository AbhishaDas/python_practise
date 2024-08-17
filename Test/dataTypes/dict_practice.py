fruit_dict={"apple":"red","mango":"yellow","avocado":"green"}

"""len of dict"""
# x=fruit_dict.__len__()
# print(x)

"""print color of mango"""
# x=fruit_dict.get("apple")
# print(x)

"""add a new fruit-color pair"""
# fruit_dict.update({"grapes":"purple"})
# print(fruit_dict)

"""remove a fruit-color pair"""
# fruit_dict.pop("avocado")
# print(fruit_dict)

"""check banana present in dict"""
# if "banana" in fruit_dict:
#     print("yes present")
# else:
#     print("not present")

"""print all keys"""
# x=fruit_dict.keys()
# print(x)

"""print all values"""
# x=fruit_dict.values()
# print(x)

"""print each fruit-color"""
# x=fruit_dict.items()
# print(x)

for x,y in fruit_dict.items():
    print(x,y)


   
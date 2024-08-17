"""defenition:  map(function, iterable)"""

"""eg using user defined fn"""
# def cube(num):
#     return num**3

# print(list(map(cube, [1,2,3,4])))

"""eg using in-build fn"""
# num_list=[1,2,-3,-4,5,6,-7,8,-9,0]

# print(list(map(abs,num_list))) """abs is a inbuild fn to find absolute value  it ignore signs)"""


#eg using lambda fn
# num_list=[1,2,-3,-4,5,6,-7,8,-9,0]
# print(list(map(lambda x:x+1, num_list)))
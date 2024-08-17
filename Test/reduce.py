from functools import reduce

def sum_list(x,y):
    print(x,y)
    return x+y 

print(reduce(sum_list, [1,2,3,4])) 


print(reduce(lambda x,y: x*y, [1,2,3,4]))
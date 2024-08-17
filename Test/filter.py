#syntax: filter(function, iterable)

def positive(num):
    return True if num>0 else False

print(list(filter(positive, [1,2,-3,4,-6,-8,0])))

#eg using lambda

print(list(filter(lambda x: x.isupper(),'AbHiSha')))
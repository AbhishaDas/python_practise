def outer_func(func):
    def inner_func(str):
        res=str.upper()
        return res
    
    return inner_func

@outer_func
def main_func(string):
    return string

result=main_func("abhishadas")
print(result)

"""decorate fn to print cube of a list"""
# def outer_fn(func):
#     def inner_fn(lst_item):
#         x=list(map(lambda x:x**3, lst_item))
#         return x
#     return inner_fn

# @outer_fn
# def main_fn(lst):
#     return lst

# x=main_fn([1,2,3,4,5])
# print(x)
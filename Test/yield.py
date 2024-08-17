"""using return"""
# def generate_num_return():
#     numbers=[]
#     for i in range(1, 4):
#         numbers.append(i)
#     return numbers
    
# number_return = generate_num_return()
# for number in number_return:
#     print(number)



"""using yield"""
def generate_num():
    for i in range(1,4):
        yield i**3

number_yield = generate_num()
for number in number_yield:
    print(number)



"""yield problem"""

# def generate_num():
#     for i in range(1,5):
#         yield i

# num_yield=generate_num()
# for num in num_yield:
#     print(num**2)

# print(next(num_yield))
# print(next(num_yield))
# print(next(num_yield))
# print(next(num_yield))
# print(next(num_yield))
# print(next(num_yield))







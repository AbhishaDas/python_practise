"""Write a program that will take the bits in a number and shift them to the left end. 
For example, 01010110 (binary) would become 11110000 (binary)."""


def shift_binary(num):
    bits=len(num)
    
    while '0' in num[1:]:
        print("Before",num)
        num= num[1:] + '0'
        print("After",num)
        
    return num




binary_num= "01010110"
result = shift_binary(binary_num)
print("Result",result)
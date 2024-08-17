def is_prime(n):
    if n<=1:
        return False

    for i in range(2,n):
        if n%i==0:
            return False
    return True
        

number=int(input("Enter a number to check prime or not: "))
if is_prime(number):
    print("Entered number is a Prime number")
else:
    print("Entered number is not a Prime number")


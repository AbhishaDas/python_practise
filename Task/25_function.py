def is_divisible_by_10(number):
    if number % 10 == 0:
        return True
    else:
        return False



num=float(input("Enter a number: "))
print(is_divisible_by_10(num))

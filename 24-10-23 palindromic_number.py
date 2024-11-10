import math

def lenght_num(n):
    return len(str(n)) 
    return math.floor(math.log10(n)) + 1    # Another way of computing the number of digits (doesn't work when n = 0)

def first_digit(n):
    return n // 10 ** (lenght_num(n)-1)

def last_digit(n):
    # If n is defined in the decimal system, the reminder of the integer division by 10 is the last digit
    return n % 10

def inner_num(n):
    # Extract the number corresponding to the inner digits of a natural number
    # Get rid of the first digit
    order = 10 ** (lenght_num(n) - 1)
    without_first = n - (first_digit(n) * order)
    # Get rid of the last digit
    without_last = without_first // 10
    return without_last

def is_palindromic_num(n):
    if lenght_num(n) == 1:
        return True
    elif lenght_num(n) == 2:
        first = first_digit(n)
        last = last_digit(n)
        return first == last
    else:
        first = first_digit(n)
        last = last_digit(n)
        inner = inner_num(n)
        return first == last and is_palindromic_num(inner)

n = int(input("Enter a number: ")) 
print(is_palindromic_num(n))
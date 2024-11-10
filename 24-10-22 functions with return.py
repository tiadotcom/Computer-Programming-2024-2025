import math

def area1(radius):
    a = math.pi * radius * 2
    return a

def area(radius):
    return math.pi * radius * 2

# Any instruction after a return cannot be executed (it's called dead code)

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
    
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    # print("dx = ", dx)
    # print("dy = ", dy)
    dsquared = dx**2 + dy**2
    # print("dsquared = ")
    result = math.sqrt(dsquared)
    return result

def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result

def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)

# Print a string n times
def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

def factorial(n):
    if n == 0:
        return 1
    # We have to be sure that the n is a natural number
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

def rec_power(base, exp):
    if exp == 0:
        return 1
    else:
        recurse = rec_power(base, exp - 1)
        result = base * recurse
        return result

# print(rec_power(2, 5))
# print(factorial(100))

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
num = 23
# print(f"The {num}th number of the Fibonacci series is:", fibonacci(num))

def fibonacci_iter(n):
    f_1 = 0
    f_2 = 1
    print(f"First {n} numbers of the Fibonacci series:")
    print(f_1)
    for i in range(2, n + 1):
        f_n = f_1 + f_2
        print(f_n)
        f_2 = f_1
        f_1 = f_n
    # return f_n

print(fibonacci_iter(5))
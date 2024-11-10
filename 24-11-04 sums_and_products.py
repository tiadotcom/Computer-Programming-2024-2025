# Write a program that takes in input from the user:
# a positive integer n
# the character 's' or 'p'
# When the user enters 's', print the sum of the integers in 1...n
# When the user enters 'p', print the product of the integers in 1...n
# Handle the cases of invalid inputs properly

def sum_and_prod(n, operator):
    sum = 0
    prod = 1
    n = int(n)
    if operator == "s":
        for i in range(1, n + 1):
            sum += i
        print(f"The sum of all integers from 1 to {n} is {sum}")

    elif operator == "p":
        for i in range(1, n + 1):
            prod *= i
        print(f"The product of all integers from 1 to {n} is {prod}")

    else:
        while(operator != "s" and operator != "p"):
            operator = input("Please insert a valid operator ('s'/'p'): ")
        sum_and_prod(n, operator)

def check_correctness_of_n(n):
    global num
    while(num == 0):
        num = float(input("Please insert an integer number bigger than 0: "))

    integer_num = int(num)
    while(num != integer_num):
        num = float(input("Please insert an integer number: "))
        integer_num = int(num)

num = float(input("Insert a positive integer: "))
check_correctness_of_n(num)
operator = input("Write 's' for sum, 'p' for product: ")
sum_and_prod(num, operator)


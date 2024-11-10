def to_binary(n):
    if n <= 1:
        return n
    return to_binary(n//2)*10 + (n%2)

n = int(input("Insert the number: "))
print("The binary representation of the number is", to_binary(n))
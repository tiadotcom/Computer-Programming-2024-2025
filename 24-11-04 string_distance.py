def string_distance():
    pass

while True:
    x = input("Insert a string: ")
    if(x.isalpha() and 3 <= len(x) <= 10):
        break
    else:
        print(f"The string '{x}' is invalid!")



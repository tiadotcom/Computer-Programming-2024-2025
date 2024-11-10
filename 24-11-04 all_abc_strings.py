def all_ABC_strings(length_left, current_string):
    if length_left == 0:
        print(current_string)
        return
    all_ABC_strings(length_left-1, current_string + "A")
    all_ABC_strings(length_left-1, current_string + "B")
    all_ABC_strings(length_left-1, current_string + "C")

l = int(input("Insert the length: "))
all_ABC_strings(l, "")

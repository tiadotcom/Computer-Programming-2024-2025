# Write a function named right_justify that takes a string named s as a parameter
# and prints the string with enough leading spaces so that the last letter of the string is in column 70
# of the display.
# Hint: Use string concatenation and repetition. Also, Python provides a built-in function called len
# that returns the length of a string, so the value of len('monty') is 5.

def right_justify(s):
    lenght = len(s)
    space = 70 - lenght
    justify = " "*space
    s = justify + s
    print(s)

right_justify("Mammal")
right_justify("1234567890123456789012345678901234567890123456789021345678901234567890")
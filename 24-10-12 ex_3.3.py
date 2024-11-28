# Write a function that draws a grid 
#  + - - - - + - - - - +

def row(a):
    for i in range(a):
        print("+ ", "- "*4, end = " ")
    print("+")

def col(a):
    for i in range(a):
        print("|", " "*9, end = " ")
    print("|")

def grid(num_r, num_c):
    for i in range(num_r): 
        row(num_c)
        for i in range(4):
            col(num_c)
    row(num_c)

num_r = int(input("How many rows? "))
num_c = int(input("How many columns? "))
grid(num_r, num_c)  


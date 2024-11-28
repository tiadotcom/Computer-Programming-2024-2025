# Game of Fifteen

from pprint import pprint
import random

# Create a matrix for storing the position of the elements
numbers = list(range(0, 16))
random.shuffle(numbers)
M = [numbers[i:i + 4] for i in range(0, 16, 4)] 

def graphic():
    print()
    print(" ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓██████████████▓▒░░▒▓████████▓▒░       ░▒▓██████▓▒░░▒▓████████▓▒░         ░▒▓█▓▒░▒▓████████▓▒░ ")
    print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓████▓▒░▒▓█▓▒░        ")
    print("░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                ░▒▓█▓▒░▒▓█▓█░░       ")
    print("░▒▓█▓▒▒▓███▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░        ░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░           ░▒▓█▓▒░▒▓███████▓▒░  ")
    print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                ░▒▓█▓▒░      ░▒▓█▓▒░ ")
    print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                ░▒▓█▓▒░      ░▒▓█▓▒░ ")
    print(" ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░       ░▒▓██████▓▒░░▒▓█▓▒░                ░▒▓█▓▒░▒▓███████▓▒░  ")
    print()

def display_matrix(M):
    """
    Pretty prints the matrix status with vertical and horizontal lines.
    """
    print("┌────┬────┬────┬────┐")
    for i in range(4):
        print(f"│ {' │ '.join(f'{M[i][j]:<2}' for j in range(4))} │")
        if i < 3:
            print("├────┼────┼────┼────┤")
    print("└────┴────┴────┴────┘")


def move_down(M, element):
    """
    This function moves an element down, provided that the slot below the element is free 
    """
    position = None
    for row in range(4):
        for column in range(4):
            if M[row][column] == element:
                position = (row, column) # stores the position of the element that we want to move down
    # print(position, position[0], position[1])
    if M[position[0] + 1][position[1]] == 0: # checks if it is possible to move the element down
        M[position[0]][position[1]] = 0
        M[position[0] + 1][position[1]] = element
    else:
        print("Error")
    display_matrix(M)

def move_up(M, element):
    """
    This function moves an element up, provided that the slot abow the element is free 
    """
    position = None
    for row in range(4):
        for column in range(4):
            if M[row][column] == element:
                position = (row, column) # stores the position of the element that we want to move down
    # print(position, position[0], position[1])
    if M[position[0] - 1][position[1]] == 0: # checks if it is possible to move the element down
        M[position[0]][position[1]] = 0
        M[position[0] - 1][position[1]] = element
    else:
        print("Error")
    display_matrix(M)

def move_left(M, element):
    """
    This function moves an element to the left, provided that the slot at the left of the element is free 
    """
    position = None
    for row in range(4):
        for column in range(4):
            if M[row][column] == element:
                position = (row, column) # stores the position of the element that we want to move down
    # print(position, position[0], position[1])
    if M[position[0]][position[1] - 1] == 0: # checks if it is possible to move the element down
        M[position[0]][position[1]] = 0
        M[position[0]][position[1] - 1] = element
    else:
        print("Error")
    display_matrix(M)

def move_right(M, element):
    """
    This function moves an element to the right, provided that the slot at the right of the element is free 
    """
    position = None
    for row in range(4):
        for column in range(4):
            if M[row][column] == element:
                position = (row, column) # stores the position of the element that we want to move down
    # print(position, position[0], position[1])
    if M[position[0]][position[1] + 1] == 0: # checks if it is possible to move the element down
        M[position[0]][position[1]] = 0
        M[position[0]][position[1] + 1] = element
    else:
        print("Error")
    display_matrix(M)

def win(M):
    """
    This function verifies if the matrix status is the winning one
    """
    numbers = list(range(1, 16))
    numbers.append(0)
    # print(numbers)
    winning_M = [numbers[i:i + 4] for i in range(0, 16, 4)] 
    # print(winning_M)
    if M == winning_M:
        print("Congrats! You won!")
        return True
    return False
 

### MAIN ###
graphic()
display_matrix(M)

while True:
    print()
    element = int(input("Enter element: "))
    move = input("Enter move ('u' / 'd' / 'l' / 'r'): ").lower()
    print()
    if move == "u":
        move_up(M, element)
    elif move == "d":
        move_down(M, element)
    elif move == "l":
        move_left(M, element)
    elif move == "r":
        move_right(M, element)
    else:
        print("Invalid move. Please enter 'u', 'd', 'l', or 'r'.")
    if win(M):
        break
   

### TEST ###
test = False # change to True in order to test the program
if test:
    display_matrix(M)
    element = int(input())
    move_down(M, element)
    element = int(input())
    move_up(M, element)
    element = int(input())
    move_left(M, element)
    win(M)
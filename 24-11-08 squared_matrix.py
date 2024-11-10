from random import randint


def generate_random_matrix(n):
    """
    Takes a positive integer n.
    Returns a square matrix of random integers in [0,9] that has size n 
    """
    M = [] # the list M will store each row of the matrix as a sublist
    for _ in range(n):
        M.append([]) # we create the sublist
        for _ in range(n):
            x = randint(0,9) # randint(a,b) returns a random integer in [a,b]
            M[-1].append(x) # each number is appended to the last row of M
    return M


def print_matrix(M):
    """
    Takes a matrix M.
    Pretty-prints M. 
    """
    n = len(M) # finds the sumber of rows in the matrix
    print("[")
    for i in range(n):
        for element in M[i]:
            print(f"{element:5}", # :5 specifies a minimum width of 5 spaces for the printed value while 
                  end = "") # at the end of the printing, Python prints "" instead of the default "\n"
        print()
    print("]")


def square(M):
    """
    Takes a matrix M.
    Returns a new matrix that is M * M. 
    """
    n = len(M)
    M_squared = [] # creates a list that will contain the rows as sublists
    for i in range(n):
        M_squared.append([]) # creates a new row
        for j in range(n):

            ### here we are calculating x = M_squared[i][j]
            x = 0
            for k in range(n):
                x += M[i][k] * M[k][j] 
            ###

            M_squared[-1].append(x)

    return M_squared


### MAIN ######################################################################


while True:
    n = int(input("Insert matrix size : "))
    if n > 0:
        break
    else:
        print(f"The size", n, "is invalid\n")

M = generate_random_matrix(n)
print("\nM = ")
print_matrix(M)

M_squared = square(M)
print("\nM^2 = ")
print_matrix(M_squared)
"""
Most of the programs are just tools for realizing a given task. In other words, they are transient.
Other programs are persistent. There is a hierarchy of ways for storing data; the most used are files and databases.
We'll use only text files, but there are also other ways to store informations on a file.

"""

fout = open("output.txt", "w") # "w" stands for writing mode
line1 = "This here's the wattle\n" # "\n" counts as one character
print(fout.write(line1)) # write() prints the number of characters written
fout.close() # in any case the file is closed at the end of the program

# "%" is the format operator
# syntax: <format string> % <format sequence> --> format string specifies how the values in format sequence are formatted and rendered
tot_camels = 52
print("I have spotted %d camels" % tot_camels) 
print("In %d years, %g %s" % (3, 10, "camels")) # %d: int  |  %g: float  |  %s: str

# string formatting
print("{}, {}, {}".format("a", "b", "c"))
print("{2}, {0}, {1}".format("a", "b", "c"))

import os
current_working_directory = os.getcwd()
print(current_working_directory)
print(os.path.exists("words.txt"))
print(os.path.exists("ciao.txt"))
print(os.path.abspath("words.txt"))
print(os.path.isdir("words.txt"))
print(os.path.isfile("emma.txt"))
print(os.listdir(current_working_directory))

def walk(directory_name):
    for name in os.listdir(directory_name):
        path = os.path.join(directory_name, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

# walk(current_working_directory)

import pickle
t = [1, 2, 3]
s = pickle.dumps(t) # encodes t
print(s)
t2 = pickle.loads(s) # decodes s
print(t2)

"""
while True:
    try:
        fin = open("bad_file.txt")
        break
    except:
        print('Something went wrong.')

while True:
    try:
        x = int(input("Insert a number: "))
        break
    except ValueError:
        print("Oops! That was not a valid number.")
        print("Try again...")

while True:
    try:
        raise KeyboardInterrupt
        break
    finally:
        print('Goodbye, world!')
"""



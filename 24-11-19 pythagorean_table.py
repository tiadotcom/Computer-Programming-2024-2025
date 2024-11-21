# We want to compute the Pythagorean table (10 x 10)
from pprint import pprint 

# List of lists
t = list()
for i in range(11):
    t.append(list())
    for j in range(11):
        t[i].append(i * j)
print("Pythagorean table (10 x 10) as a list of lists")
for row in t:
    print(row)
print()

# Dictionary of dictionaries
d = dict()
for i in range(11):
    d[i] = dict()
    for j in range(11):
        d[i][j] = i * j
print("Pythagorean table (10 x 10) as a dictionary of dictionaries")
for key, value in d.items():
    print(f"{key}: {value}")
print()

# Dictionary with bidimentional keys
d2 = dict()
for i in range(11):
    for j in range(11):
        d2[i, j] = i * j
print("Pythagorean table (10 x 10) as a dictionary with bidimensional keys")
for key, value in d2.items():
    print(f"{key}: {value}")



### Other operations with tuples ###
L = [1, 3, 2]
print(L.sort())
t = tuple(L)
print(t)

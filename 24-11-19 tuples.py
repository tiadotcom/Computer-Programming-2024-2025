"""
Tuples are very similar to lists. 
A tuple object is an immutable sequence of values; its elements are indexed by integers.
"""

t = ()
print(type(t))

t = ("a", "b", "c")
t = "a", "b", "c" # parenthesis are not necessary
print(t)

t = "x", # a single-element tuple is written as a string with a comma at the end
print(type(t))

t = tuple("hi mum")
print(t)

dictionary = {"key1": "value1", "key2": "value2"}
t = tuple(dictionary)
print(t)

list1 = ["element1", "element2", "element3"]
t = tuple(list1)
print(t)
print(f"2nd element: {t[1]}")

# t[0] = "changed_element1" leads to an error because tuples does not support item assignment 

t = ("changed_element1",) + t[1:] 
print(t)

# Comparison is possible between tuples
print(f"(0, 1, 2) < (0, 3, 4): {(0, 1, 2) < (0, 3, 4)}")
print(f"(0, 1, 2) < (0, 0, 4): {(0, 1, 2) < (0, 0, 4)}")
print(f"(0, 1, 9999) < (0, 3): {(0, 1, 9999) < (0, 3)}")
print(f"(0, 1) < (0, 3, 4): {(0, 1) < (0, 3, 4)}")
print(f"(1, 2) = (1, 2, 3): {(1, 2) == (1, 2, 3)}")
print(f"(1, 2, 3) = (1, 2, 3): {(1, 2, 3) == (1, 2, 3)}")

# Swapping the value of two variables 
a = "first_element"
b = "second_element"
temp = a
a = b
b = temp
print(a, b)

# Swapping the value of two variables using tuple assignment
a = "first_element"
b = "second_element"
a, b = b, a
print(a, b)

# Splitting a string with tuples
addr = "monty@python.org"
uname, domain = addr.split("@")
print(uname, domain)

# Tuple as a return value
t = divmod(7, 3)
print(t)

quot, rem = divmod(7, 3)
print(quot, rem)

def printall(*args):
    print(args)
    return args
a = printall(3, "a", True)
print(type(a), a)

t = (7, 3)
divmod(*t) # "*" is the scattering operator
print(divmod(*t))

def multi_as_list():
    return [2, True]
[a, b] = multi_as_list()
print(a, b)

def multi_as_string():
    return "AB"
[a, b] = multi_as_string()
print(a, b)

s = "abcd"
t = [0, 1, 2]
for pair in (zip(s, t)):
    print(pair)
list1 = zip("12345", "abcde")
for pair in list1:
    print(pair)
print(list(zip("1234", "abcd")))  

def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False
t1 = [1, 2, 3]
t2 = [4, 2, 5]
print(has_match(t1, t2))
print(has_match("abc", "xbx"))
print(has_match("abc", "xxx"))

for index, element in enumerate("abc"):
    print(index, element)

# Using a list of tuples to initialize a new dictionary
t = [("a", 0), ("b", 1), ("c", 2)]
d = dict(t)
print(d)

last = "Doe"
first = "John"
number = "123-456-7890"
directory = {}
directory[last, first] = number
for last, first in directory:
    print(first, last, directory[last, first])
for name in directory:
    print(name, directory[name])

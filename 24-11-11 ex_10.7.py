# Write a function called has_duplicates that takes a list and returns True if there
# is any element that appears more than once. It should not modify the original list.

def has_duplicates(t):
    return len(t) != len(set(t)) # set() converts the list to a set, automatically removing duplicates

t = [1, 2, 6, 8, 2]
print(has_duplicates(t))
t = ["a", "n", "c", "n", "c", "r"]
print(has_duplicates(t))
t = [5, 6, 2]
print(has_duplicates(t))
t = ["g", "j"]
print(has_duplicates(t))
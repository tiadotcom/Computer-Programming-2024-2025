# Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending order
# and False otherwise.

def is_sorted(t):
    t_aux = list(t)
    t_aux.sort()
    return t_aux == t

t1 = [1, 2, 7]
t2 = ["b", "a"]
t3 = [1, 9, 2]
print(is_sorted(t1))
print(is_sorted(t2))
print(is_sorted(t3))
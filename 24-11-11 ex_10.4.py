# Write a function called chop that takes a list, modifies it by removing the first and last elements, and returns None. 

def chop(t):
    t.pop(0)
    t.pop(len(t) - 1)
    print(t)
    return None

t = [1, 2, 3, 4, 5, 6]
chop(t)
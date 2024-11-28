# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

def middle(t):
    L = len(t)
    t1 = []
    if t:
        for i in range(1, L-1):
            t1.append(t[i])
    return t1
    
t = [1, 2, 3, 4, 5, 6]
print(middle(t))
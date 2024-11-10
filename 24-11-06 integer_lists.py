# Create a list containing the integers from 1 to 30
    # Remove from the list all the even numbers
    # Remove from the list all the multiples of 5
# Write a function that, given a list of integers, removes all the multiples of a given number k

L = [] # Empty list
# L = list() is another way for creating an empty list
for i in range(1, 31):
    L.append(i) # Adds the elements to the list
print(f"From 1 to 30: {L}")

# Remove the even numbers from L
t = []
for n in L:
    if n % 2 != 0: # The number is odd
        t.append(n)
print(f"No even: {t}")

# Another way to remove the even numbers
t2 = L
for n in t2:
    if n % 2 == 0:
        t2.remove(n)
print(f"No even: {t2}")

# Remove all the multiples of 5
t1 = []
for n in L:
    if n % 5:
        t1.append(n)
print(f"No even, no multiples of 5: {t1}")

# General function for removing the multiples of k
def remove_multiples(L, k):
    t = []
    for n in L:
        if n % k:
            t.append(n)
    print(f"No multiples of {k}: {t}")

L1 = []
for i in range(1, 31):
    L1.append(i)
remove_multiples(L1, 3)

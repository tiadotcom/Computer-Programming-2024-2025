# Create a list L containing the integers from 2 to N
# Initialize a list P containing 1
# While L is not empty
    # Remove the first element of L and assign it to k
    # Append k to P
    # Remove the multiples of k from L
# Print P

def remove_multiples(L, k):
    t = [] # Aux list
    for n in L:
        if n % k:
            t.append(n)
    return t

N = 100
L = []
for i in range(2, N + 1):
    L.append(i)

P = [1]

while L: # It's the same as saying while L != []
    k = L.pop(0) # Extract the first element from L and assigns it to k
    P.append(k)
    L = remove_multiples(L, k)

print(f"Prime numbers in 1 to {N}: {P}")
print(f"Number of primes in 1 to {N}: {len(P)}")
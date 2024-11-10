# Check whether a string is palindrome or not

# Recursive method
def is_palindrome_rec(s):
    if not(s): # String is empty
        return True # The empty string is palindrome
    elif len(s) == 1:
        return True
    else: # Recursion step
        return s[0] == s[-1] and is_palindrome_rec(s[1 : len(s) - 1])

# Iterative method
def is_palindrome_iter(s):
    result = True
    L = len(s)
    for i in range(int(L/2)):
        result = result and s[i] == s[L - 1 - i]
        # s[i] == s[- (i + 1)]
    return result

def is_palindrome_while(s):
    L = len(s)
    result = True
    left = 0
    right = L-1
    while left < right:
        result = result and s[right] == s[left]
        left = left + 1
        right = right - 1
    return result



s = input("Write something: ")
print("Recursion: ", is_palindrome_rec(s))
print("Iteractive: ", is_palindrome_iter(s))
print("While: ", is_palindrome_while(s))
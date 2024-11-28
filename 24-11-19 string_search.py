# String search with dict
"""
    Stores strings as keys in a dictionary to use the in operator
    as a fast way to check whether a string is in the dictionary.
    Compare this method with others based on list.
"""

def in_bisect(L, w):
    """
        Test if the word w is in the list L.
        Implements the binary search.
        
        L: sorted list of words
        return True if w is in L, otherwise False
    """

    if L:
        start = 0
        end = len(L)-1
        while start < end:
            middle = (end + start)//2
            if w < L[middle]:
                end = middle
            elif w > L[middle]:
                start = middle+1
            else:
                return True
        return w == L[start]
    else:
        return False
    
# Binary search on a list of strings (recursive version)
def in_bisect_rec(L, w):
    """
        Test if the word w is in the list L.
        Implements the binary search.
        
        L: sorted list of words
        return True if w is in L, otherwise False
    """

    if L:
        middle = len(L)//2
        if w < L[middle]:
            return in_bisect_rec(L[:middle], w)
        elif w > L[middle]:
            return in_bisect_rec(L[middle+1:], w)
        else:
            return True
    else:
        return False


#### MAIN #####

# Reads the words from a file and initialize the dictionary using the words as keys.
filename = "words.txt"
print('Read the words from file', filename)
fin = open(filename)
d = {}
for line in fin:
    word = line.strip()
    d[word] = ""

# Put the strings in a list for testing
print('Put the words in a list, L')
L = list()
for w in d.keys():
    L.append(w)

# DEBUG #
L2 = sorted(L)
if (L == L2):
    print('The list L2 is sorted (and binary search can be applied on it)')
print('L == L2:', L == L2, '   L2 is L:', L2 is L)
print('Notice that although L could be already sorted, the search algorithm may not consider this property')

# TEST # 
import time

print(f'TESTS - search all the words in L ({len(L)} elements) using several methods')
# Test 1: search all the strings in L using the in operator on the list
print('Test 1: search using the "in" operator on the list L')
t1 = time.time()
for s in L:
    v = s in L
t2 = time.time() 
print('\t', 'Time:', t2 - t1, 's')

# Test 2: search all the strings in L using the binary search on the sorted list
print('Test 2: search using the binary search on the sorted list L2')
t1 = time.time()
for s in L:
    v = in_bisect(L2, s)
t2 = time.time() 
print('\t', 'Time:', t2 - t1, 's')

# Test 3: search all the strings in d using the in operator on the dict keys
t1 = time.time()
for s in L:
    v = s in d
t2 = time.time() 
print('Test 3: search using the "in" operator on the dict')
print('\t', 'Time:', t2 - t1, 's')

# Test 4: search all the strings in L using the recursive binary search on the sorted list
print('Test 4: search using the recursive binary search on the sorted list L2')
t1 = time.time()
for s in L:
    v = in_bisect_rec(L2, s)
t2 = time.time() 
print('\t', 'Time:', t2 - t1, 's')

# Test 5: search all the strings in L using the bisect.bisect() function on the sorted list
import bisect
print('Test 5: search using bisect.bisect on the sorted list L2')
t1 = time.time()
for s in L:
    r = bisect.bisect(L2, s)
# Elapsed time in seconds since t.
t2 = time.time()
print('\t', 'Time:', t2 - t1, 's')

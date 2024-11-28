# Metathesis pairs
"""
    Read the list of words from words.txt,
    and print the metathesis pairs, i.e., words that differs for only
    two swapping letters.
    
    Uses the dictionary of anagrams lists to keep the number of
    comparisons low.
"""

def create_anagrams_dict(filename):
    fin = open(filename)
    d = {}
    for line in fin:
        word = line.strip()
        # NB: sorted returns a list
        #k = str(sorted(word))
        k = "".join(sorted(word))
        
        if k in d:
            d[k].append(word)
        else: 
            d[k] = [word]

    return d

def hamming_distance(s1, s2):
    d = 0
    for a, b in zip(s1,s2):
        if not a == b:
            d += 1
    return d

#### MAIN #####

# Read the words from a file and initialize the dictionary
# using the words as keys.

d = create_anagrams_dict('words.txt')

import time
# find the anagrams that differs for only two letters

# first method: carefully organize the comparisons to avoid
#               multiple tests
t1 = time.time()
meta = []
for k in d:
    if len(d[k]) > 1:
        d[k].sort()
        for i in range(0, len(d[k])-1):
            w1 = d[k][i]
            for j in range(i+1, len(d[k])):
                w2 = d[k][j]
                # w1 <= w2
                if hamming_distance(w1, w2) == 2:
                    #print(w1, w2)
                    meta.append((w1, w2))
meta.sort()
print('elapsed time 1st method:', time.time()-t1, 'seconds')

# second method: evaluate all the possible pairs, but filtering
t1 = time.time()
meta2 = []
for k in d:
    if len(d[k]) > 1:
        for w1 in d[k]:
            for w2 in d[k]:
                # use short circuit evaluation to avoid to compute
                # twice the Hamming distance of the same pair
                if w1 < w2 and hamming_distance(w1, w2) == 2:
                    #print(w1, w2)
                    meta2.append((w1, w2))
meta2.sort()
print('elapsed time 2nd method:', time.time()-t1, 'seconds')

print()
print('1st method, 2nd method, is output the same?')
print(len(meta), len(meta2), meta == meta2)


# Anagrams
"""
    Read the list of words from words.txt, create a dictionary
    with the anagrams, and print the longest anagrams list of 8 letters.
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

def print_longest_anagrams_first(d):
    """
    Print the lists of anagrams in order of the
    (reverse) length of the lists.
    """ 
    t = []
    for k in d:
        l = len(d[k])
        t.append((l, d[k]))
    t.sort(reverse = True)

    # print the words with at least three anagrams
    for l in t:
        if (l[0] > 3):
            print(l[1])

#### MAIN #####

# Read the words from a file and initialize the dictionary
# using the words as keys.

d = create_anagrams_dict('words.txt')

# filter the dictionary with the 8-letter words
d_8 = {}
for k in d:
    if len(k) == 8:
        d_8[k] = d[k]
print_longest_anagrams_first(d_8)

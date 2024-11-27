# Anagrams
"""
    Read the list of words from words.txt, create a dictionary
    with the anagrams, and print the anagrams ordered by the
    number of anagrams.
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


#### MAIN #####

# Read the words from a file and initialize the dictionary
# using the words as keys.

d = create_anagrams_dict('words.txt')

# create the dictionary with the number of the anagrams in the key
length_dict = {}
for k in d:
    n = len(d[k])
    if n in length_dict:
        length_dict[n].append(d[k])
    else:
        length_dict[n] = [d[k]]

t = list(length_dict.keys())
t.sort(reverse = True)

### print the words with at least three anagrams
##for l in t:
##    if (l > 3):
##        for words in length_dict[l]:
##            print(words)

t = []
for k in d:
    l = len(d[k])
    t.append((l, d[k]))
t.sort(reverse = True)

# print the words with at least three anagrams
for l in t:
    if (l[0] > 3):
        print(l[1])


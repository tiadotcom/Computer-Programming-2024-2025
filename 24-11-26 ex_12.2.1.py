# Anagrams
"""
    Read the list of words from words.txt and create a dictionary
    with the anagrams.
"""


#### MAIN #####

# Read the words from a file and initialize the dictionary using the words as keys.

print('Read the words from file')
fin = open("words.txt")
d = {}
for line in fin:
    word = line.strip()
    # NB: sorted returns a list
    # k = str(sorted(word))
    k = "".join(sorted(word))
    
    if k in d:
        d[k].append(word)
    else: 
        d[k] = [word]

# print the words with at least three anagrams
for k in d:
    if len(d[k]) > 2:
        print(d[k])

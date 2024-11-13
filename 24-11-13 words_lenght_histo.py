### BASIC NOTIONS ###
"""
fin = open("words.txt")
line = fin.readline()
word = line.strip()
print(line)
print("...")
print(word)

fin = open("words.txt")
word1 = fin.readline().strip()
print(word1)
"""

# Build the histogram of the words having the same lenght. Use a list, where the element indexed by i contains the number of words composed of i characters
filename = "words.txt"
fin = open(filename)
histo = [] # we are using lists, not dictionary
# histo = [0, 3, 1, 5] means that there are 0 words of lenght 0, 3 words of lenght 1, one word of lenght 2 and 5 words of lenght 3
for line in fin:
    word = line.strip()
    word_lenght = len(word)
    if word_lenght < len(histo): # histo[word_lenght] already exists
        histo[word_lenght] += 1 
    else: # histo[wordlenght] does not exist yet
        num_zeros = word_lenght - len(histo) + 1
        histo += [0] * num_zeros
        histo[word_lenght] = 1
print(histo)
    
# Build the histogram of the words having the same lenght. The lenght of the words is the key of the dictonary item that contains the list of those words
filename = "words.txt"
fin = open(filename)
fin = sorted(fin) 
histo = {}
for line in fin:
    word = line.strip()
    word_lenght = len(word)
    if word_lenght in histo:
        histo[word_lenght].append(word)
    else:
        histo[word_lenght] = histo.get(word_lenght, []) + [word]
print(histo)

# Merge two dictionaries adding the values for common keys
d1 = {'red': 10, 'blue': 4, 'green': 6}
d2 = {'blue': 31, 'green': 3, 'yellow': 5}
print()
for key in d1:
    if key in d2:
        d2[key] += d1[key]
    else:
        d2[key] = d1[key]
print(d2)
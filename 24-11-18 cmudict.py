# Download the Carnegie Mellon Pronouncing Dictionary
# Create a dictionary having the words as keys and the list of the phonemes as values.

from pprint import pprint
d = {}
# fin = open("cmudict.txt")
fin = open("cmudict1.txt") 
for line in fin:
    line = line.split("#")[0].strip() # when a "#"" is found, splits the line and keeps only the first part
    word = line.strip().split(" ") 
    L = len(word)
    for phonem in range(L):
        delimiter = " "
        pronunciation = delimiter.join(word)
    d.update({word[0]: pronunciation[((len(word[0])) + 1):]})
    # print(f"\n {word[0]} {pronunciation[((len(word[0])) + 1):]}")
# pprint(d)

# Given a word, find the rhyming words (those having the same last two phonemes)
rhymes = {}
values = dict.values(d)
# print(sorted(values))
fin = open("cmudict1.txt") 
for line in fin:
    line = line.split("#")[0].strip() 
    word = line.strip().split(" ") 

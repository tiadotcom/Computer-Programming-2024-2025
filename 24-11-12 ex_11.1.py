# Write a function that reads the words in words.txt and stores them as keys in a dictionary.
# It doesn’t matter what the values are.
# Then you can use the in operator as a fast way to check whether a string is in the dictionary.

from pprint import pprint

file = open("words.txt")

def stores_words(file):
    for line in file:
        key = line.strip()
        d[key] = "value"
    return d

def check_string(d, s):
    return s in d # returns True if the string is in the dictionary

d = dict()
s = "imposter"
pprint(stores_words(file))
print(check_string(d, s))
# To check whether a word is in the word list we can speed things up with a bisection search (also known as binary search).
# You start in the middle and check to see whether the word you are looking for comes before the word in the middle of the list. 
# If so, you search the first half of the list the same way. Otherwise you search the second half.
# Either way, you cut the remaining search space in half. 
# Write a function called in_bisect that takes a sorted list and a target value and returns True if
# the word is in the list and False if it’s not.

def in_bisect(t, word):
    s = t[:]
    s.sort()
    if len(s) % 2 == 0:
        middle_word = s[int(len(s) / 2) + 1]
        
    else:
        middle_word = s[len(s) / 2]


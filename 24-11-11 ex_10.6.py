# Two words are anagrams if you can rearrange the letters from one to spell the other.
# Write a function called is_anagram that takes two strings and returns True if they are anagrams.

def is_anagram(t1, t2):
    t1 = t1.replace(" ", "").lower()
    t2 = t2.replace(" ", "").lower()
    return sorted(t1) == sorted(t2)

t1 = "listen"
t2 = "silent"
print(is_anagram(t1, t2))
t3 = "sileno"
print(is_anagram(t1, t3))
t4 = "Dormitory"
t5 = "Dirty room"
print(is_anagram(t4, t5))
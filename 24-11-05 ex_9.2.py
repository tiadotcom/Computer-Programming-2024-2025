# Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it.
# Write a program that reads words.txt and prints only the words that have no “e”. 
# Compute the percentage of words in the list that have no “e”.

def has_no_e(word):
    global count_e
    test = True
    for i in range(len(word)):
        if word[i] == "e":
            test = False
            count_e += 1
    if test:
        print(word)

fin = open("words (1).txt")
count_e = 0
count_words = 0
for line in fin:
    word = line.strip()
    has_no_e(word)
    count_words += 1
perc = round(((count_words - count_e) / count_words * 100), 2)
print(f"Number of words = {count_words}")
print(f"Number of words with no 'e' = {count_words - count_e}")
print(f"Percentage of words without 'e' = {perc}%")
    
            

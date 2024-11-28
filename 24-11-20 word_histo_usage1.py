# Counts words in emma.txt
import string
from pprint import pprint

fin = open("emma.txt", encoding = "utf-8")
header_end_marker = "***"
footer_start_marker = "FINIS"

# def most_used(histo, how_many = 100):
    # return sorted(histo.items(), key = lambda item: item[1], reverse = True)[:how_many]

def most_used(histo, how_many=100):
    word_list = [] # create an empty list to store words and their count
    
    # Turn the dictionary into a list of (word, count) pairs
    for word in histo:
        word_list.append((word, histo[word]))
    
    # Sort the list manually (from highest to lowest count)
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if word_list[i][1] < word_list[j][1]:  # compare counts
                word_list[i], word_list[j] = word_list[j], word_list[i]  # swap
    
    # Take only the top 'how_many' items
    top_words = []
    for i in range(how_many):
        if i < len(word_list):  # ensure we don’t go out of bounds
            top_words.append(word_list[i])

    return top_words

# Skip the cover, i.e. skip all the lines up to the one starting with "***"
for line in fin:
    line.strip()
    if line.startswith(header_end_marker): 
        break

# Process the book
w_histo = {}
for line in fin:
    line.strip()
    if line.startswith(footer_start_marker): 
        break
    else:
        for s in string.punctuation + '”' + '“':
            line = line.replace(s, " ")
        L = line.split()
        for w in L:
            w = w.lower() 
            # Update the histogram
            if w in w_histo:
                w_histo[w] += 1
            else:
                w_histo[w] = 1

pprint(w_histo)
print(f"\nThe name of the protagonist appears {w_histo["emma"]} times")
max_used = 0
max_used_w = ""
for w in w_histo:
    if w_histo[w] > max_used:
        max_used = w_histo[w]
        max_used_w = w
print(f"\nMax used word: '{max_used_w}' ({max_used} times)")
print("\nList of the 100 most used words: ")
pprint(most_used(w_histo))


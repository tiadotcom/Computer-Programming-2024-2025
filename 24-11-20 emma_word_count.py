# Counts words in emma.txt
import string
from pprint import pprint

fin = open("emma.txt", encoding = "utf-8")
header_end_marker = "***"
footer_start_marker = "FINIS"

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
print(w_histo["emma"])
max_used = 0
max_used_w = ""
for w in w_histo:
    if w_histo[w] > max_used:
        max_used = w_histo[w]
        max_used_w = w
print(f"Max used word: '{max_used_w}' ({max_used} times)")

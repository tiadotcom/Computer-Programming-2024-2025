fin = open("words (1).txt")
for line in fin: # Line works as i
    word = line.strip()
    if len(word) > 20:
        print(word)

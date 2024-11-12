# Write a function that reads the file words.txt and builds a list with one element per word.
# Write two versions of this function, one using the append method and the other using the idiom t = t + [x]. 
# Which one takes longer to run? Why?

fin = open("words.txt")
def append_method():
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)
    print(t)

def idiom_method():
    t = []
    for line in fin:
        word = line.strip()
        t = t + [word]
    print(t)

append_method()
idiom_method()


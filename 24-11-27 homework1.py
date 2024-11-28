# Given a filename, print new lines, words and characters count

fin = open("words.txt")
number_of_lines = 0
number_of_words = 0
number_of_characters = 0
for line in fin:
    number_of_lines += 1
    line = line.strip()
    number_of_characters += len(line) 
    words = line.split(" ")
    for word in words:
        number_of_words += 1
print(f"There are {number_of_lines} lines")
print(f"There are {number_of_words} words")
print(f"There are {number_of_characters} characters")




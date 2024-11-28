# Create a list L with the words in words (1).txt
L = open("words (1).txt").read().split("\n")

# Create the list of the elements in L which are 5 characters long
five_letters = [L]
for w in L:
    if len(w) == 5:
        five_letters.append(w)
print("\n\n\n\n\n")
print(len(five_letters))
print(five_letters)

# Create the list of the 5-character words having the letter "a" as the middle character
five_letters_a_middle = []
for w in five_letters:
    if w[2] == "a":
        five_letters_a_middle.append(w)
print("\n\n\n\n\n")
print(len(five_letters_a_middle))
print(five_letters_a_middle)

five_letters_a_middle_no_r = []
for w in five_letters_a_middle:
    if not "r" in w:
        five_letters_a_middle_no_r.append(w)
print("\n\n\n\n\n")
print(len(five_letters_a_middle_no_r))
print(five_letters_a_middle_no_r)
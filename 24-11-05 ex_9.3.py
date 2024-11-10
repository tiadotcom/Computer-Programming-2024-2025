# Write a function named "avoids" that takes a word and a string of forbidden letters, 
# and that returns True if the word doesn’t use any of the forbidden letters.
# Write a program that prompts the user to enter a string of forbidden letters and 
# then prints the number of words that don’t contain any of them.

def not_good_avoids(word, forb):
    global count_forb
    test = True
    for i in range(len(word)):
        for j in range(len(forb)):
            if word[i] == forb[j] and test:
                test = False # If the word uses one of the forbidden letters, the test variable will be assigned False
                count_forb += 1

def avoids(word, forb):
    for letter in word:
        if letter in forb:
            return False
    return True

forb = input("Enter a string of forbidden letters: ")
fin = open("words (1).txt")
count_forb_words = 0

for line in fin:
    word = line.strip()
    if avoids(word, forb):  # If the word passes the forbidden test, the function will return True and the if statements will be read
        count_forb_words += 1
        # print(word)

print(f"There are {count_forb_words} words that don't contain any of the forbidden letters")


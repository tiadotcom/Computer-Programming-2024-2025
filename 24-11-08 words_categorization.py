# Read the words contained in the file words.txt
# Print the number of words that do not start with a vowel

# Categorize the words that start with a vowel dividing them by first letter and then on second letter.
# Print their categorization as shown in the execution example.
# The words in each group are printed alphabetically sorted.
# Don't print the groups containing 0 words.

fin = open("words.txt")
vowels = ["a", "e", "i", "o", "u"]
count_dont_start_with_wowel = 0

def create_matrix():
    M = []
    for _ in range(5):  
        row = []  
        for _ in range(26):  
            row.append([]) # creates a row with 26 sublist
        M.append(row) # adds the row to the matrix 
    return M

def print_matrix(M):
    for i in range(5):
        print(vowels[i], ": {")
        for j in range(26):
            if M[i][j]: # only prints non-empty lists
                second_letter = chr(ord("a") + j)
                words_joined_by_commas = ", ".join(sorted(M[i][j]))
                print("\t", second_letter, ": {", words_joined_by_commas, "}")
    print("}")

M = create_matrix()

for line in fin:
    word = line.strip()
    first_letter = word[0]

    # first letter is not a vowel
    if first_letter not in vowels: 
        count_dont_start_with_wowel += 1

    # first letter is a vowel
    else:
        f_l = vowels.index(first_letter)
        second_letter = word[1]
        s_l = ord(second_letter) - ord("a")
        M[f_l][s_l].append(word)

print(f"There are {count_dont_start_with_wowel} words that do not start with a wovel")
print_matrix(M)
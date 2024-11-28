# Read the first 100 words from a text file and print them in four columns (columnwise).
# Supposing a screen width of 80 characters, try to distribute the columns evenly.

fin = open("words.txt")
number_of_words = 0
all_words = []

for line in fin:
    word = line.strip().split()
    all_words.extend(word)

first_100_words = all_words[:100]

"""
for i in range(0, 100, 4):
    # 4 columns, 20 characters wide

    # print the first word
    print("%-20s" % first_100_words[i][0], end = "")

    # print the second word
    i += 1
    print("%-20s" % first_100_words[i][0], end = "")

    # print the third word
    i += 1
    print("%-20s" % first_100_words[i][0], end = "")

    # print the fourth word
    i += 1
    print("%-20s" % first_100_words[i][0])
"""

with open("empty.txt", "w") as fout:
    for i in range(0, 100, 4):
        for j in range(4):
            if i + j < len(first_100_words):  
                # print(f"{first_100_words[i + j]:<20}", end = "")
                print("%-20s" % first_100_words[i + j], end = "")
                fout.write("%-20s" % first_100_words[i + j])
        print()
        fout.write("\n")


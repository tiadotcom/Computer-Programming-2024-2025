# Write a program that:
    # Simulates the rolling of a six-sided die
    # Builds the histogram of the results

import random
from pprint import pprint

number_of_rolls = 200
histo = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
for roll in range(number_of_rolls):
    number = int(random.randint(1, 6))
    histo[number] += 1
pprint(histo)

for number in histo:
    print(f"{number}: {'■' * histo[number]}")

# Simulate the rolling of two six-sided dies
number_of_rolls2 = 200
histo2 = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
for roll in range(number_of_rolls2):
    number1 = int(random.randint(1, 6))
    number2 = int(random.randint(1, 6))
    result = number1 + number2
    histo2[result] += 1
print()
pprint(histo2)

for number in histo2:
    if number < 10:
        print(f"{number}:  {'■' * histo2[number]}")
    else:
        print(f"{number}: {'■' * histo2[number]}")
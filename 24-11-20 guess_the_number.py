# Write a program that:
    # Generates a secret integer in [1, 100]
    # Iteratively asks the user to guess the number
    # Provides additional information at each attempt (bigger or smaller)
    # Terminates the game at the right guess, or after 10 guesses

import random

number = random.randint(1, 100) # generates a random integer in [1, 100]
# print(number)
print("A secret number has been generated!")
number_of_guesses = 10 # can be modified
guessed = False # starting condition

for attempt in range(1, number_of_guesses + 1):
    guess = int(input("Guess the number: ")) 

    if guess == number:
        print("Congrats! You guessed the number! 😁")
        guessed = True
        break

    elif attempt < number_of_guesses:  # provide hints only if it is not the last attempt
        if guess < number:
            print(f"The secret number is bigger than {guess}.")
        else:
            print(f"The secret number is smaller than {guess}.")

if not guessed:
    print(f"Close but no cigar... you didn't guess the number😔. The correct number was {number}.")
# This exercise pertains to the so-called Birthday Paradox, which you can read about at http://en.wikipedia.org/wiki/Birthday_paradox.
# If there are 23 students in your class, what are the chances that two of them have the same birthday?
# You can estimate this probability by generating random samples of 23 birthdays and checking for matches. 
# Hint: you can generate random birthdays with the randint function in the random module.

from __future__ import print_function, division
import random

def generate_random_birthday(n):
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t

def has_duplicates(t):
    s = t[:]
    s.sort()
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False

def count_matches(num_students, num_simulations):
    count = 0
    for i in range(num_simulations):
        t = generate_random_birthday(num_students)
        if has_duplicates(t):
            count += 1
    return count

num_students = 23
num_simulations = 190
count = count_matches(num_students, num_simulations)
percentage = (count / num_simulations) * 100

print(f"After {num_simulations} simulations with {num_students} students there were {count} simulations with at least one match")
print(f"After {num_simulations} simulations the percentage that at least two students out of 23 share the same birthay is {int(percentage)}%")
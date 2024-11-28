# Functions have a name and some arguments. They possibly provide a value. 
# import math imports the module math
# We can compose functions. A function can invoke another function

print("Now, the lumberjack song")

def print_lyrics():
    print("I am a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

print("Ready?")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

b=10
c=342

def increment(value):
    t = 'Here!'
    value = value + 1
    print(value)

increment(b)
increment(c)


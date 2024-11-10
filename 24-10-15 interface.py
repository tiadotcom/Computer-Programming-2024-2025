import turtle
import math
bob = turtle.Turtle()

# Make the function more general by using parameters
def square(t, lenght):
    for i in range(4):
        t.fd(lenght)
        t.lt(90)
square(bob, 100)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
polygon(bob, 7, 70)
# polygon(bob, n=7, length=70)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, n, length)
circle(bob, 100)

turtle.done()
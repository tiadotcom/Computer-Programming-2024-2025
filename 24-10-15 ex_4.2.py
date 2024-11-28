# Write an appropriately general set of functions that can draw flowers as in Figure 4.1
import turtle
import math

bob = turtle.Turtle()

def petal(t):
    bob.lt(90)
    bob.speed(0)
    for i in range(3):
        for i in range(10):
            bob.fd(20)
            bob.rt(6)
        bob.rt(120)
        for i in range(10):
            bob.fd(20)
            bob.rt(6)
    bob.rt(60)
    for i in range(3):
        for i in range(10):
            bob.fd(20)
            bob.rt(6)
        bob.rt(120)
        for i in range(10):
            bob.fd(20)
            bob.rt(6)

petal(bob)

turtle.done()
import turtle
bob = turtle.Turtle()

def square():
    bob.speed(5)
    for i in range(4):
        bob.fd(100)
        bob.lt(90)

def circle_360():
    bob.speed(10)
    bob.pencolor("red")
    bob.color("yellow")
    for i in range(360):
        bob.fd(3)
        bob.lt(1)

def circle_720():
    bob = turtle.Turtle()
    bob.speed(400)
    bob.fd(200)
    for i in range(720):
        bob.fd(0.5)
        bob.lt(0.5)

bob = turtle.Turtle()
circle_360()

turtle.done()


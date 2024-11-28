import turtle

# bob = turtle.Turtle()
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)

# for i in range(4):
    # bob.fd(100)
    # bob.lt(90)

# for side in rage(1, 100. 10):
    # square(bob, side)

def dont_open():
    bob = turtle.Turtle()
    bob.rt(90)
    bob.fd(100)
    bob.pencolor('red')
    def square():
        for i in range (2):
            bob.fd(100)
            bob.pencolor('blue')
            bob.lt(90)
            bob.fd(100)
            bob.pencolor('red')
            bob.lt(90)
    square()
    bob.rt(90)
    bob.fd(100)
    square()
    bob.rt(90)
    bob.fd(300)
    for i in range (3):
        bob.rt(90)
        bob.fd(100)
    bob.rt(180)
    bob.fd(100)
    bob.rt(90)
    bob.fd(200)

bob = turtle.Turtle()

# S
def letter_s():
    bob.lt(180)
    bob.pencolor("red")
    for i in range(2):
        bob.fd(20)
        bob.lt(90)
    bob.fd(20)
    for i in range(2):
        bob.rt(90)
        bob.fd(20)
    bob.bk(20)
    bob.lt(180)

# V
def letter_v1():
    bob.pencolor("white")
    bob.fd(20)
    bob.pencolor("orange")
    bob.lt(105)
    bob.fd(41)
    bob.bk(41)
    bob.rt(30)
    bob.fd(41)
    bob.bk(41)

# V
def letter_v2():
    bob.pencolor("white")
    bob.fd(20)
    bob.pencolor("green")
    bob.lt(105)
    bob.fd(41)
    bob.bk(41)
    bob.rt(30)
    bob.fd(41)
    bob.bk(41)

# E
def letter_e():
    bob.pencolor("white")
    bob.rt(75)
    bob.fd(20)
    bob.pencolor("yellow")
    bob.lt(90)
    bob.fd(40)
    bob.rt(90)
    bob.fd(20)
    bob.bk(20)
    for i in range(2):
        bob.rt(90)
        bob.fd(20)
        bob.lt(90)
        bob.fd(20)
        bob.bk(20)
    bob.fd(20)

# A
def letter_a():
    bob.rt(75)
    bob.pencolor("white")
    bob.fd(20)
    bob.pencolor("blue")
    bob.lt(75)
    bob.fd(40)
    bob.rt(150)
    bob.fd(40)
    bob.rt(180)
    bob.fd(20)
    bob.lt(75)
    bob.fd(10)
    bob.bk(10)
    bob.lt(105)
    bob.fd(20)
    bob.pencolor("white")
    bob.fd(100)

letter_s()
letter_v1()
letter_e()
letter_v2()
letter_a()

turtle.done()


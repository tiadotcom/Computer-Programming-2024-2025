# Use turtle to simulate a laser reflection in a mirror box
import turtle

# Box
min_x = -200
max_x = 200
min_y = -100
max_y = 100

# Prepare the turtle
box = turtle.Turtle()
box.pencolor("blue")
box.pensize(10)
box.penup()

# Move the box turtle to the top-right vertex
box.fd(max_x)
box.lt(90)
box.fd(max_y)
box.lt(90)

# Start to draw the box
box.pendown()
box.fd(max_x - min_x)
box.lt(90)
box.fd(max_y - min_y)
box.lt(90)
box.fd(max_x - min_x)
box.lt(90)
box.fd(max_y - min_y)
box.lt(90)
box.hideturtle()

# Choose the initial direction of the laser
laser = turtle.Turtle()
laser.pencolor("red")
laser.speed(0)
laser.pensize(3)
angle = 70
laser.lt(angle)

# Setup for the simulation
step = 5
max_step = 1000

# Compute reflection
for t in range(max_step):
    laser.fd(step)
    if laser.xcor() >= max_x:
        # Laser reached the right wall
        laser.lt(180 - 2 * laser.heading())
    if laser.ycor() >= max_y:
        # Laser reached the top wall
        laser.rt(2 * laser.heading())
    if laser.xcor() <= min_x:
        # Laser reached the left wall
        laser.rt(2 * laser.heading() - 180)
    if laser.ycor() <= min_y:
        # Laser reached the bottom wall
        laser.lt(-2 * laser.heading())

turtle.done()
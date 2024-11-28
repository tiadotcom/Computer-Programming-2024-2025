# Using turtle, simulate a laser trajectory to hit (or miss) a target.
import turtle
import math

box = turtle.Turtle() # Turtle for the box
target = turtle.Turtle() # Turtle for the target
laser = turtle.Turtle() # Turtle for the laser
box.hideturtle()
target.hideturtle()
laser.hideturtle()

# Draw the box boundaries
min_x = -300
max_x = 300
min_y = -300
max_y = 300

box.penup()
box.goto(min_x, max_y)
box.pendown()
box.pencolor("black")
box.speed(0)

for _ in range(2):
    box.forward(max_x - min_x)
    box.right(90)
    box.forward(max_y - min_y)
    box.right(90)

# Draw the target
target_center_x = 150
target_center_y = 100
radius = 20

target.penup()
target.goto(target_center_x, target_center_y - radius)
target.pendown()
target.speed(0)
target.pencolor("green")
target.fillcolor("green")
target.begin_fill()
target.circle(radius)
target.end_fill()

# Set up the laser
angle = 42
step = 10
max_steps = 10000
hit = False

laser.penup()
laser.goto(0, 0)  # Starting position of the laser
laser.setheading(angle)  # Initial angle of the laser in degrees
laser.pendown()
laser.pencolor("red")
laser.speed(0)
laser.showturtle()

# The laser moves until it hits the target
def stops_after_hitting():
    global hit

    # Simulate laser movement with reflection
    while(not hit):
        laser.forward(step)

        # Check if the laser hits the target 
        distance = math.sqrt((laser.xcor() - target_center_x) ** 2 + (laser.ycor() - target_center_y) ** 2)
        if distance <= radius:
            print("The laser hit the target!")
            hit = True
            break

        # Check for collisions with box walls and reflect
        if laser.xcor() >= max_x or laser.xcor() <= min_x:
            laser.setheading(180 - laser.heading())
        if laser.ycor() >= max_y or laser.ycor() <= min_y:
            laser.setheading(-laser.heading())

# The laser moves until it reaches max_steps. The program prints the number of hits
def stops_after_max_steps():
    global hit
    hits = 0  # Initialize the counter for hits

    # Use a for loop to iterate up to max_steps
    for i in range(max_steps):
        laser.forward(step)

        # Check if the laser is inside the target radius
        distance = math.sqrt((laser.xcor() - target_center_x) ** 2 + (laser.ycor() - target_center_y) ** 2)

        if distance <= radius:
            # If the laser was not already inside the target, count a hit
            if not inside_target:
                hits += 1
            inside_target = True
        else:
            # The laser is outside the target, reset the flag
            inside_target = False

        # Check for collisions with box walls and reflect
        if laser.xcor() >= max_x or laser.xcor() <= min_x:
            laser.setheading(180 - laser.heading())
        if laser.ycor() >= max_y or laser.ycor() <= min_y:
            laser.setheading(-laser.heading())

    # Print the total number of hits after the simulation ends
    print(f"The laser hit the target {hits} time(s)")

# The laser moves until it hits the target n times
def stops_after_hitting_n_times(n):
    global hit
    hits = 0

    # Simulate laser movement with reflection
    while(not hit):
        laser.forward(step)

        # Check if the laser hits the target 
        distance = math.sqrt((laser.xcor() - target_center_x) ** 2 + (laser.ycor() - target_center_y) ** 2)
        if distance <= radius:
            print(f"The laser hit the target {n} times!")
            hit = True
            hits += 1
            if hits >= n:
                break

        # Check for collisions with box walls and reflect
        if laser.xcor() >= max_x or laser.xcor() <= min_x:
            laser.setheading(180 - laser.heading())
        if laser.ycor() >= max_y or laser.ycor() <= min_y:
            laser.setheading(-laser.heading())

stops_after_hitting()
turtle.done()
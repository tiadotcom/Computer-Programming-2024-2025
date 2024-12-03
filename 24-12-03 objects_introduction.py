
### OBJECT ORIENTING PROGRAMMING ###

# Define a class
class Point:
    """ Represents a point in 2D space """
    def print_point(self):
        print('(%g, %g)' % (self.x, self.y)) 
    def __init__(self,x=0.0,y=0.0): 
        self.x = x
        self.y = y
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

print("print(Point) =", Point) # The output is "<class '__main__.Point'>", because Point is a class defined in the main script
print("print(int) =", int) # The output is "<class 'int'>" 

# Define an object
blank = Point() # blank is called the instance of Point
print("print(blank) =", blank) # The output is "<__main__.Point object at 0x00000219B7B25F10>

# Define an attribute
blank.x = 3
blank.y = 4
blank.RandomWord = 22
a = Point()
# Writing print(a.x) leads to an error because a.x was not instanciated

print("print(blank.x) =", blank.x) # The output is "3"
print("print(blank.RandomWord) =", blank.RandomWord)
x = blank.x
print("print(x) =", x)
print("blank.x is x:", blank.x is x)

import math
distance = math.sqrt(blank.x ** 2 + blank.y ** 2)
print("distance =", distance)

def print_point(p):
    print("attributes =", "(%g, %g)" % (p.x, p.y))
print("blank ", end = "")
print_point(blank)
print("blank attributes printed as method = ", end = "")
blank.print_point()

# Build a rectangle
class Rectangle:
    """ Represents a rectangle

        Attributes: width, height, corner
    """

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width / 2
    p.y = rect.corner.y + rect.height / 2
    return p
center = find_center(box)
print("center ", end = "")
print_point(center)

box.width = box.width + 50
box.height = box.height + 100
def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight
print(f"initial size of rect = {box.width}, {box.height}")
grow_rectangle(box, 50, 100)
print(f"final size of rect = {box.width}, {box.height}")

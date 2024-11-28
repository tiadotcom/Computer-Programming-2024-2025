# Drawing flowers with python
# We want to know: the number of the petals, the lenght of the petal and the angle (let's say, the thickness) of the petal

# Position the turtlimport turtle
# Draw one petal
# Turn of a suitable angle
# Repeat for all the petals

import math
import turtle
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


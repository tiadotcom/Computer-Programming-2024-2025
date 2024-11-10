# Newton's approximation of the square root
import math

def mysqrt(a):
    # Returns the Newton's approximation of the square root of a 
    precision = .001 # Accuracy needed
    x = a # Initial guess
    y = (2 * x) + precision
    while abs(x - y) >= precision:
        x = y
        y = (x + a/x) / 2
    return y # Returns the last computed approximation

# a = int(input("Insert a number: "))
# y = mysqrt(a)
# print(f"Newton's approx of sqrt({a}) = {y}")

def formatting_str(s, field):
    return s + " " * (field - len(s))

# Characters needed for the table
a_field = 3
mysqrt_field = 20
sqrt_field = 20
diff_field = 20

# Print the header
a_header = "a"
a_str = formatting_str(a_header, a_field)
mysqrt_header = "mysqrt(a)"
mysqrt_str = formatting_str(mysqrt_header, mysqrt_field)
sqrt_header = "math.sqrt(a)"
sqrt_str = formatting_str(sqrt_header, sqrt_field)
diff_header = "diff"
diff_str = formatting_str(diff_header, diff_field)

# for a in range(1, 10):
    # y = mysqrt(a)
    # print(f"Newton's approximation of sqrt({a}) = {y}   Precise value of sqrt({a}) = {math.sqrt(a)}   Difference = {y - math.sqrt(a)}")

print(a_str, mysqrt_str, sqrt_str, diff_str)
print("-" * a_field, "-" * mysqrt_field, "-" * sqrt_field, "-" * diff_field)
for a in range(1, 10):
    y = mysqrt(a)
    sqrt_a = math.sqrt(a)
    diff = abs(y - sqrt_a)
    print(formatting_str(str(a), a_field),
          formatting_str(str(y), mysqrt_field),
          formatting_str(str(sqrt_a), sqrt_field),
          formatting_str(str(diff), diff_field))



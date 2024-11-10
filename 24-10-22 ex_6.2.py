#Ackermann function A(m, n)

def ackermann_function(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        result = ackermann_function(m - 1, 1)
        return result
    elif m > 0 and n > 0:
        result = ackermann_function(m - 1, ackermann_function(m, n - 1))
        return result
    
ackermann_function(3, 4)

    
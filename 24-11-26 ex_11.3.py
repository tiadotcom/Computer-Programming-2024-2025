# Implementations of the Ackerman function computation.
#
# - ackermann(): normal recursion
# - ackermann_memo1(): with a memo being a two-level dictionary
#                       using integers as keys at both the levels
# - ackermann_memo2(): with a memo being a dictionary using a string
#                       encoding of the function parameters
# - ackermann_memo3(): with a memo being a dictionary using a tuple
#                       of the parameters as key

import sys
sys.setrecursionlimit(10**6)
memo = {}

def ackermann(m, n):
    """
    Computes the Ackermann function:
                /
               |  n+1,                if m = 0                                                         
    A(m, n) = <   A(m-1, 1),          if m > 0 and n = 0
               |  A(m-1, A(m, n-1)),  if m > 0 and n > 0     
                \
                
    n, m: non-negative integers
    
    See http://en.wikipedia.org/wiki/Ackermann_function
    """

    if m == 0:
        return n+1
    elif n == 0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))

memo = {}
def ackermann_memo1(m, n):
    """
    Computes the Ackermann function using memo.
    The memo is a two-level dictionary using integers as keys at both
    the levels:
    A(m, n) --->  memo[m][n]
    """
    
    if m in memo:
        if n in memo[m]:
            return memo[m][n]
    else:
        memo[m] = dict()

    if m == 0:
        return n+1
    elif n == 0:
        a = ackermann_memo1(m-1, 1)
        memo[m][n] = a
        return a
    else:
        a = ackermann_memo1(m-1, ackermann_memo1(m, n-1))
        memo[m][n] = a
        return a


def key_str(m, n):
    return str(m) + ',' + str(n)

def ackermann_memo2(m, n):
    """
    Computes the Ackermann function using memo.
    The memo is a dictionary using a string encoding of the
    function parameters (computed with key_str()) as key:
    A(m, n) --->  memo[key_str(m, n)]
    """
    key = key_str(m, n) 
    
    if key in memo:
        return memo[key]

    if m == 0:
        return n+1
    elif n == 0:
        a = ackermann_memo2(m-1, 1)
        memo[key] = a
        return a
    else:
        a = ackermann_memo2(m-1, ackermann_memo2(m, n-1))
        memo[key] = a
        return a

def ackermann_memo3(m, n):
    """
    Computes the Ackermann function using memo.
    The memo is a dictionary using a tuple of the parameters as key:
    A(m, n) --->  memo[m, n]
    """

    if (m, n) in memo:
        return memo[m, n]

    if m == 0:
        return n+1
    elif n == 0:
        a = ackermann_memo3(m-1, 1)
        memo[m, n] = a
        return a
    else:
        a = ackermann_memo3(m-1, ackermann_memo3(m, n-1))
        memo[m, n] = a
        return a


######### MAIN ########
memo = {}
m = 3
n = 5
print('A(', m, ',', n, '): ', ackermann(m, n))
print('A(', m, ',', n, '): ', ackermann_memo3(m, n))

memo = {}
m = 3
n = 8 # for 9 exceed recursion
#print('A(', m, ',', n, '): ', ackermann(m, n))
print('A(', m, ',', n, '): ', ackermann_memo3(m, n))

for m in range(1, 4):
    for n in range(1, 6000):
        print('A(', m, ',', n, '): ', ackermann_memo3(m, n))
    

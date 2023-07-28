# HW01 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/hw/hw01/

# Q1 (syllabus check)





# Q2: A Plus Abs B
from operator import add, sub

def a_plus_abs_b(a, b):
    # Return a + abs(b), but without calling abs.
    # >>> a_plus_abs_b(2, 3)
    # 5
    # >>> a_plus_abs_b(2, -3)
    # 5    
    if b >= 0:
        h = add
    else:
        h = sub
    return h(a, b)
print(a_plus_abs_b(2, 3))
print(a_plus_abs_b(2, -3))





# Q3: Two of Three
def two_of_three(x, y, z):
    # Return a*a + b*b, where a and b are the two smallest members of the
    # positive numbers x, y, and z.
    # >>> two_of_three(1, 2, 3)
    # 5
    # >>> two_of_three(5, 3, 1)
    # 10
    # >>> two_of_three(10, 2, 8)
    # 68
    # >>> two_of_three(5, 5, 5)
    # 50
    return (min(x, y, z) * min(x, y, z)) + (((x + y + z) - ((min(x, y, z) + (max(x, y, z))))) * ((x + y + z) - ((min(x, y, z) + (max(x, y, z))))))

print(two_of_three(1, 2, 3))





# Q4: Largest Factor
def largest_factor(x):
    # Return the largest factor of x that is smaller than x.

    # >>> largest_factor(15) # factors are 1, 3, 5
    # 5
    # >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    # 40
    # >>> largest_factor(13) # factor is 1 since 13 is prime
    # 1
    x # (placeholder)
        
# My answer for Project Euler number 3, which also works for this HW question 
def primeFactors(x):
    index = 2
    primes = []
    while index <= x:
        if x % index == 0:
            primes.append(index)
            x = x / index
        else:
            index += 1
    return primes

# Q5: If Function vs Statement

# Q6: 
def hailstone(x):
    n = 1
    while x != 1:
        print(x)
        if ((x % 2) == 0):
            x = x / 2
        else:
            x = (x * 3) + 1
    print(x)
    return n

"""Example of Fib sequence"""
def fib(n):
    """Compute the nth Fibonacci number, for n >= 2."""
    pred, curr = 0, 1   # Fibonacci numbers 1 and 2
    k = 2               # Which Fib number is curr?
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

positive = -9
negative = -12
while negative:
   if positive:
       print(negative)
   positive += 3
   negative += 3

def sum_digits(x):
    length = x
    while length > 0:
        x = (x-(x-1))
        length - 1

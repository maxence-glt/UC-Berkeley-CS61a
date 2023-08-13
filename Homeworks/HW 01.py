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

    num, index = x, 0
    while index < x:
        if (x % num == 0) and (x != num):
            index += (x + 1)
            return num
        else:
            num -= 1
    return num

        
# My answer for Project Euler number 3, which also works for this HW question 
# but is overkill due to the nature of this problem


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



# Q5: Lost my original answer, will come back to this one one day! 
#    (already answered the original question in SICP anyways)



# Q6: Hailstone
def hailstone(x):
    sum = 1
    while x != 1:
        print(x)
        if ((x % 2) == 0):
            x = x // 2
            sum += 1
        else:
            x = (x * 3) + 1
            sum += 1
    print(1)
    return "With a length of " + str(sum)

# hailstone(10)
# 10
# 5
# 16
# 8
# 4
# 2
# 1

# Longest Hailstone is 77031 for numbers <100,000 with a length of 351 (https://rosettacode.org/wiki/Hailstone_sequence)
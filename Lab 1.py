# Lab 1 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/lab/lab01/

# Q1 - Q3 (WWPD don't have coding)

# Q4: Fix the Bug
def both_positive(a, b):
    return a> 0 and b > 0





# Q5: Sum Digits
def sum_digits(x):
    sum, index = 0, 10
    while x > 10:
        sum = sum + (x % index)
        x = x // index
    return sum + x
sum_digits(1234567890)





# Q6: WWPD
# Q7 and Q8 are "extra practice"

# Q7: Falling Factorial
def falling(n, k):
    multiples = 1
    while k >= 0:
        if k == 0:
            return multiples
        else: 
            multiples = multiples * n
            n -= 1
            k -= 1
    return multiples





# Q8: Double Eights
def double_eights(n):
    while n > 1:
        if n <= 87:
            return False
        if (n % 10) == ((n % 100) % 10):
            return True
        else: 
            n = (n // 10)
    
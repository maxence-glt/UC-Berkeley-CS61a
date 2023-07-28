"""Q3"""

from operator import add, mul, mod

def lambda_curry2(func):
    return lambda x: lambda y: func(x, y)

"""guerilla discussion"""

def count_digits(n):
    total = 1
    while n >= 0:
        if n == 0:
            return n
        if n < 10 and n != 0:
            return total
        else:
            n = n // 10
            total = total + 1
    return total

"""THIS ONE WAS SO HARD"""

def count_matches(n, m):
    total = 0
    while n >= 0:
        remainder = n % 10
        remainder2 = m % 10
        if (n and m >= 0) and (remainder == remainder2):
            total = total + 1
        if  n <=0 or m <= 0:
            return total
        n = n // 10
        m = m // 10
    return total

def make_skipper(n):
    i = 1
    def f(y):
        i = 1
        while i <= y:
            if (i % n) == 0:
                i = i + 1
            else:
                print(i)
                i = i + 1
    return f   

a = make_skipper(13)
a(14)


def ordered_digits(x):
    while x > 0:
        trueFalse
        total = x % 10
        y = (x // 10) % 10
        if total > y:
            trueFalse = "True"
            
        else:
            trueFalse = "False"
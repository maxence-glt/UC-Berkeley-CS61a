# Guerilla 0 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/disc/guer00.pdf





# 2.3
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





# 2.4
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





# 4.5
def make_skipper(n):
    def f(y):
        i = 1
        while i <= y:
            if (i % n) == 0:
                i = i + 1
            else:
                print(i)
                i = i + 1
    return f   





# 5.1
def ordered_digits(x):
    while x > 0:
        total1 = x % 10
        total2 = (x % 100) // 10
        if total1 >= total2:
            trueFalse = "True"
            x = x // 10
        else:
            trueFalse = "False"
            x = x - x
    return trueFalse





# 5.2 
def cycle(f1, f2, f3):
    def my_cycle(i):
        def identity(b):
            total, num = 1, 1
            for a in range(0, i + 1):
                if a == 0:
                    total = total * b
                else:
                    if num == 1:
                        total = f1(total)
                        num += 1
                    elif num == 2:
                        total = f2(total)
                        num += 1
                    elif num == 3:
                        total = f3(total)
                        num = 1
            return total
        return identity
    return my_cycle
# Discussion 3 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/disc/disc03.pdf

# 1.1
def multiply(m, n):
    total = 0
    if m == 0 or n == 0:
        return 0
    else:
        total = m + multiply(m, n-1)
        return total
    
# 1.3
def hailstone(n):
    print(int(n))
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(3 * n + 1)
    
# 1.4
def is_prime(n):
    k = 2
    return prime_helper(n, k)
    
def prime_helper(n, k):
    if n == 1:
        return False
    elif n % k == 0:
        return False  
    else: 
        (prime_helper(n, k + 1))
    return True

# Question 1.5     
def merge(n1, n2):
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10        





# 1.6 (optional)
def make_func_repeater(f, x):
    def repeat(y):
        if y == 0:
            return x
        else:
            return f(repeat(y - 1))
    return repeat